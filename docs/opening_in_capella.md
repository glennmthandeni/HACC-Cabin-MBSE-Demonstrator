# Opening the project in Capella 7.1.0

## Import

1. Start Capella 7.1.0 and select a workspace.
2. Open `File → Import → General → Existing Projects into Workspace`.
3. Choose **Select root directory**.
4. Select the repository folder `model/HACC_MBSE_Architecture`.
5. Confirm that `HACC_MBSE_Architecture` is selected and finish the import.
6. Open `HACC_MBSE_Architecture.aird`.

Use a separate workspace if a project with the same name is already present.

## Project files

| File | Role |
|---|---|
| `.project` | Eclipse project definition |
| `HACC_MBSE_Architecture.afm` | Capella viewpoint metadata |
| `HACC_MBSE_Architecture.capella` | Semantic architecture model |
| `HACC_MBSE_Architecture.aird` | Sirius session and 18 native representations |

The four files use canonical names because the `.aird` session references the
`.capella` and `.afm` resources by those names. Keep them together.

## Navigate the portfolio

Expand the semantic model through:

1. Operational Analysis;
2. System Analysis;
3. Logical Architecture;
4. Physical Architecture;
5. EPBS Architecture.

The native representations are available beneath the `.aird` session. Start with
the OEBD and OAB, then follow the SAB, LAB and PAB. Open the mode/state-machine
view for seated, bed-mode and fail-passive behaviour. Functional-chain views show
the same principal flows at successive architecture levels.

## Validation

Run Capella's **Validate** action after semantic changes. From the repository root,
run `python qa/validate_portfolio.py` to check file naming, cross-file references,
register synchronization and portfolio completeness. The portable checker does
not replace Capella's rule engine or engineering verification.

