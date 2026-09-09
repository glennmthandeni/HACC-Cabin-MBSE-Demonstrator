# Engineering basis

## Design problem

The InnovAero task defines a 3.0 × 2.0 × 2.3 m VIP cabin compartment in a
carbon-laminate long-haul aircraft. It asks for acoustic assessment, material
selection and integration, seated and reclined evaluation, and additional comfort
measures. The HACC architecture addresses the low-frequency transmission problem
identified in the team's Final Technical Report.

## Selected architecture

| Design element | Defined basis |
|---|---|
| Full enclosure barrier | Six faces, 2.0 kg/m² limp-mass layer |
| Upper-face porous treatment | 100 mm melamine |
| Floor treatment | 25 mm melamine under the floor finish |
| Dominant bay | 125 mm full fill, local CLD, +1.0 kg/m² overlay |
| Tuned treatment | Serviceable 97/120/149 Hz resonator cassette |
| Seated active control | Two structural references, two sources and two error microphones |
| Bed-mode active control | Secondary transducer array with seat-position handover |
| Passive concept mass | 135.0 kg before design growth |
| Passive plus active mass | 147.5 kg before design growth |

The architecture is fail-passive: active-system loss, disablement or fault response
returns the occupant to passive protection. The state model defines seated,
bed-mode, degraded, muted and passive-only behaviour, together with recovery paths.

## Performance basis

The Final Technical Report distinguishes field-incidence power transmission loss
from the direct-path pressure model used for passenger-level estimates. The
selected passive architecture improves the representative 200 Hz condition by
about 15.4 dB and the 100–500 Hz design band by about 8.1 dB.

With the conservative active-control design allocation, the reported estimates are:

| Metric | Seated | Reclined / bed mode |
|---|---:|---:|
| Representative 200 Hz level | 55.3–60.1 dB(A) | 60.1–62.1 dB(A) |
| Balanced broadband screening level | 73.2–78.1 dB(A) | 78.0–80.1 dB(A) |

These values are design estimates, not installed measurements. The architecture
therefore maintains explicit verification gates for material properties, coupon
correlation, mock-up integration, active-control stability and matched flight test.

## Source set

Primary project sources:

1. Lufthansa Technik, *InnovAero 2026 Competition Task*.
2. KPR LuxAero, *Hybrid Acoustic Comfort Cell Final Technical Report*, 2026.

Supporting acoustics references used by the engineering study include:

- D. T. Blackstock, *Fundamentals of Physical Acoustics*.
- D. A. Bies and C. H. Hansen, *Engineering Noise Control: Theory and Practice*.
- L. E. Kinsler et al., *Fundamentals of Acoustics*.
- L. L. Beranek and T. J. Mellow, *Acoustics: Sound Fields and Transducers*.
- T. J. Cox and P. D'Antonio, *Acoustic Absorbers and Diffusers*.

The source documents are cited here and are not redistributed in this repository.

