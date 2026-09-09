# Model scope

## Purpose

The HACC Cabin MBSE Demonstrator presents the systems-engineering transformation
of an aircraft-cabin acoustic concept through the ARCADIA lifecycle. The system of
interest is the Hybrid Acoustic Comfort Cell: passive, resonant and active measures
that improve VIP passenger acoustic comfort during long-haul cruise.

## BASE architecture

BASE content is derived from the KPR LuxAero HACC Final Technical Report and the
InnovAero 2026 task. It includes:

- passenger comfort in seated and lie-flat configurations;
- the aircraft acoustic environment and transmission paths;
- passive enclosure, dominant-bay treatment and tuned resonator;
- structural references, ear-side error sensing and dual-mode secondary sources;
- ANC control, protection, seat-mode handover and crew disable;
- health monitoring, local diagnostics, maintainability and fail-passive operation;
- architecture constraints and verification cases tied to the engineering report.

## EXT architecture

EXT elements exercise controlled extension of the system boundary:

- read-only HACC status for a representative cabin-management system;
- selected health and diagnostic records for a representative ground-maintenance
  service.

EXT exchanges are architecture definitions. They do not prescribe a proprietary
message schema, aircraft bus, cabin-management implementation or ground-service
protocol.

## Model boundary

The model includes operational, functional, logical, physical and behavioural
architecture. It represents component exchanges, boundary ports and delegation,
physical behaviour deployment and an aggregate configuration item.

The following are outside scope:

- detailed aircraft-network and wiring implementation;
- production mechanical drawings and structural substantiation;
- supplier configuration control below the aggregate HACC item;
- executable FxLMS software and calibrated controller coefficients;
- complete IFE, SATCOM or cabin-management architecture;
- certification approval or guaranteed installed acoustic performance.

## Modelling conventions

Requirements and stakeholder needs are implemented as native Capella core
`Constraint` objects. The requirements register and traceability matrix expose
their identifiers, sources, verification cases and direct model anchors. The
project does not depend on the optional Requirements viewpoint.

System boundaries are represented through functional exchanges, component
exchanges, ports and realization/delegation relationships. The interface register
records those exchanges. Detailed `ExchangeItem` payload definitions are reserved
for protocol and data-contract refinement.

Physical functions are allocated to behaviour components, and behaviour parts are
deployed to node parts. This separates responsibility from installed hardware and
keeps logical realization on the behaviours that perform it.

