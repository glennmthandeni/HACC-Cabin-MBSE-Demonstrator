# Architecture inventory

## Native representations

The Sirius session contains 18 editable Capella representations:

| Architecture evidence | Count |
|---|---:|
| Operational Entity Breakdown | 1 |
| Operational Architecture Blank | 1 |
| System Architecture Blank | 1 |
| Logical Architecture Blank | 1 |
| Physical Architecture Blank | 1 |
| Mode/State Machine | 1 |
| Operational functional-chain descriptions | 3 |
| System functional-chain descriptions | 3 |
| Logical functional-chain descriptions | 3 |
| Physical functional-chain descriptions | 3 |

## Semantic content

| Element family | Count |
|---|---:|
| Semantic objects with IDs | 1,870 |
| Operational activities | 12 including root |
| System functions | 27 |
| Logical functions | 27 |
| Physical functions | 27 |
| Functional exchanges | 87 |
| Functional chains / operational processes | 12 |
| Component exchanges | 72 |
| Component ports | 126 |
| Port realizations | 175 |
| Logical components | 20 including root and actors |
| Physical components | 42 including root and actors |
| Physical behaviour-to-node deployments | 14 |
| Requirement constraints | 19 |
| ANC operating states | 7 |
| State transitions | 18 |
| Aggregate configuration items | 1 |

The counts describe serialized model content and are also available in
`model_summary.json` for automated checks.

## Functional chains

Three connected flows are represented at each architecture level:

1. passive acoustic attenuation;
2. active-control update;
3. health and maintenance reporting.

The active-control chain represents one bounded update. Feedback paths remain
visible in the functional architecture, while mode transitions and fault responses
are defined by the ANC state model.

