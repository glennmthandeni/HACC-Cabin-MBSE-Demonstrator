#!/usr/bin/env python3
"""Read-only integrity checks for the HACC GitHub portfolio."""
from pathlib import Path
from collections import Counter
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'model' / 'HACC_MBSE_Architecture'
XSI = '{http://www.w3.org/2001/XMLSchema-instance}type'
XMI = '{http://www.omg.org/XMI}type'
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def xtype(element):
    return (element.get(XSI) or element.get(XMI) or '').split(':')[-1]

def rows(relative):
    with (ROOT / relative).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))

required_files = [
    'README.md', 'LICENSE',
    'model/HACC_MBSE_Architecture/.project',
    'model/HACC_MBSE_Architecture/HACC_MBSE_Architecture.afm',
    'model/HACC_MBSE_Architecture/HACC_MBSE_Architecture.capella',
    'model/HACC_MBSE_Architecture/HACC_MBSE_Architecture.aird',
    'requirements/requirements.csv', 'requirements/traceability_matrix.csv',
    'interfaces/component_exchanges.csv',
    'verification/verification_cases.csv',
]
for name in required_files:
    check((ROOT / name).is_file(), 'Missing required file: ' + name)

try:
    model = ET.parse(PROJECT / 'HACC_MBSE_Architecture.capella').getroot()
    session = ET.parse(PROJECT / 'HACC_MBSE_Architecture.aird').getroot()
    metadata = ET.parse(PROJECT / 'HACC_MBSE_Architecture.afm').getroot()
    project = ET.parse(PROJECT / '.project').getroot()

    elements = [e for e in model.iter() if e.get('id')]
    id_counts = Counter(e.get('id') for e in elements)
    ids = {e.get('id'): e for e in elements}
    check(all(value == 1 for value in id_counts.values()), 'Semantic model contains duplicate IDs')
    check(project.findtext('name') == 'HACC_MBSE_Architecture', 'Eclipse project name is not canonical')
    vp = metadata.find('viewpointReferences')
    check(vp is not None and vp.get('version') == '7.1.0', 'Capella viewpoint version is not 7.1.0')

    resources = [e.text for e in session.iter() if e.tag.endswith('semanticResources')]
    check(resources == ['HACC_MBSE_Architecture.afm', 'HACC_MBSE_Architecture.capella'], 'Session resources are not canonical')
    for resource in resources:
        check((PROJECT / resource).is_file(), 'Session resource is missing: ' + str(resource))

    local_ref_count = 0
    for element in elements:
        for value in element.attrib.values():
            for token in value.split():
                if token.startswith('#'):
                    local_ref_count += 1
                    check(token[1:] in ids, 'Unresolved semantic reference: ' + token)

    session_refs = []
    for element in session.iter():
        href = element.get('href', '')
        if href.startswith('HACC_MBSE_Architecture.capella#'):
            session_refs.append(href.split('#', 1)[1])
    check(len(session_refs) >= 1, 'Session has no references into the semantic model')
    for target in session_refs:
        check(target in ids, 'Unresolved session-to-model reference: ' + target)
    representations = [e for e in session.iter() if xtype(e) == 'DRepresentationDescriptor']
    check(len(representations) == 18, f'Expected 18 native representations, found {len(representations)}')

    constraints = {e.get('id'): e for e in elements if xtype(e) == 'Constraint'}
    req = rows('requirements/requirements.csv')
    traces = rows('requirements/traceability_matrix.csv')
    check(len(req) == len(constraints) == 19, 'Requirement register and model constraint counts differ')
    check(len({r['ID'] for r in req}) == len(req), 'Requirement IDs are not unique')
    trace_by_req = {}
    for trace in traces:
        trace_by_req.setdefault(trace['Requirement_ID'], set()).add(trace['Element_UUID'])
        check(trace['Element_UUID'] in ids, 'Trace references an unknown model element')
        check(trace['Constraint_UUID'] in constraints, 'Trace references an unknown constraint')
    for requirement in req:
        constraint = constraints.get(requirement['Constraint_UUID'])
        check(constraint is not None, 'Requirement has no matching native constraint: ' + requirement['ID'])
        if constraint is not None:
            direct = {x.lstrip('#') for x in constraint.get('constrainedElements', '').split()}
            check(direct == trace_by_req.get(requirement['ID'], set()), 'Direct anchors differ from traceability register: ' + requirement['ID'])
            body = constraint.findtext('ownedSpecification/bodies')
            check(body == requirement['Requirement / Need'], 'Requirement text differs from native constraint: ' + requirement['ID'])

    exchanges = {e.get('id') for e in elements if xtype(e) == 'ComponentExchange'}
    interface_rows = rows('interfaces/component_exchanges.csv')
    check(len(interface_rows) == len(exchanges) == 72, 'Component-exchange register count differs from the model')
    check({r['Component_Exchange_UUID'] for r in interface_rows} == exchanges, 'Component-exchange register does not cover the model exactly')

    verification = rows('verification/verification_cases.csv')
    check(len(verification) == 16, 'Expected 16 verification cases')
    check(all(v['Status'] == 'PLANNED' and v['Result'] == 'Not assessed' for v in verification), 'Verification status is inconsistent')
    requirement_ids = {r['ID'] for r in req}
    for case in verification:
        check(set(case['Requirement_IDs'].split(';')) <= requirement_ids, 'Verification case references an unknown requirement: ' + case['ID'])

    diagram_names = [
        '01_OEBD_Operational_Context.png', '02_OAB_Operational_Architecture.png',
        '03_SAB_System_Architecture.png', '04_LAB_Logical_Architecture.png',
        '05_PAB_Physical_Architecture.png', '06_MSM_ANC_Fail_Passive_Behaviour.png',
        '07_SFCD_Active_Control_Update.png',
    ]
    for name in diagram_names:
        check((ROOT / 'diagrams' / name).is_file(), 'Missing exported diagram: ' + name)
    for path in ROOT.rglob('*'):
        check(not re.search(r'\(\d+\)', path.name), 'Copy suffix remains in repository filename: ' + str(path.relative_to(ROOT)))

    result = {
        'status': 'PASS' if not errors else 'FAIL',
        'capella_version': '7.1.0',
        'semantic_elements_with_ids': len(ids),
        'local_semantic_references_checked': local_ref_count,
        'session_model_references_checked': len(session_refs),
        'native_representations': len(representations),
        'requirement_constraints': len(constraints),
        'traceability_rows': len(traces),
        'component_exchanges': len(exchanges),
        'verification_cases': len(verification),
        'exported_diagrams': len(diagram_names),
        'errors': errors,
        'note': 'Integrity and synchronization check; engineering verification remains governed by the verification register.',
    }
except (OSError, ET.ParseError, KeyError, AttributeError) as exc:
    result = {'status': 'FAIL', 'errors': errors + [str(exc)]}

print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(0 if result['status'] == 'PASS' else 1)
