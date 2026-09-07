# Claim and Evidence Ledger

One row in the evidence-relations table represents **one evidence → claim relationship**, not an entire claim. A single CLM may have many evidence rows and many sources. See the [provenance model](../docs/provenance.md).

## Claim registry

| CLM ID | Exact claim | Claim type | Claim status | Manuscript location | Supersedes/replaced by | Notes |
|---|---|---|---|---|---|---|

Claim status: DRAFT / UNVERIFIED / SUPPORTED / MIXED / CONTRADICTED / RETRACTED.

Claim type: empirical, theoretical, conceptual, normative, or researcher inference.

## Evidence relations

| CLM ID | SRC ID | STUDY ID | Relation | Directness | Access | Locator | Appraisal / evidence quality & limits | Source version/status | Action |
|---|---|---|---|---|---|---|---|---|---|

Relation: SUPPORTS / CONTRADICTS / LIMITS / CONTEXTUALIZES.

Directness: DIRECT / INDIRECT / SECONDARY.

Access: FULL_TEXT / PARTIAL / ABSTRACT_ONLY / METADATA_ONLY / UNAVAILABLE.

Action: retain, qualify, seek more evidence, split the claim, or retract.

## Claim-level synthesis

For a substantive claim, summarize after inspecting the evidence relations:

| CLM ID | Supporting pattern | Counterevidence | Alternative explanation | Boundary conditions | Remaining unknown | Decision/DEC |
|---|---|---|---|---|---|---|

Do not treat the number of sources as an automatic measure of evidence strength. A real source may still fail to support the claim, and several reports may belong to the same STUDY.
