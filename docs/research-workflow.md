# Research Workflow

This workflow is a project convention. Stages may repeat when evidence changes a decision. See the [quality gates](quality-gates.md). Drafts and memos may be created throughout the process without changing academic readiness by themselves.

In a RESEARCH project, every substantive task begins from an active Issue and follows the [Git workflow](git-workflow.md). File outputs enter `main` through PR, review, and merge. Save an Issue checkpoint at the end of a session; use parent/child Issues when one stage contains several independently reviewable outputs. Upstream TEMPLATE maintenance is not a research stage.

| Stage | Decision question | Typical artifact | Skill |
|---|---|---|---|
| 0. Context | What are the mandate, constraints, and feasibility? | Project brief and uncertainty list | framing |
| 1. Problem | What remains unexplained and why does it matter? | Problem memo and research questions | framing |
| 2. Mapping | Which debates and concepts are relevant? | Initial literature map and terminology | evidence, theory |
| 3. Protocol | How will evidence be gathered transparently? | Review protocol, selection/appraisal plan | evidence |
| 4. Evidence | What do the sources actually report, and what are their limits? | Search log, screening, source notes, claim ledger | evidence |
| 5. Synthesis | Which explanations survive counterevidence? | Debate map and contribution audit | theory |
| 6. Design | What evidence can answer the question defensibly? | Method decision record, design matrix, analysis plan, ethics/data plan | design |
| 7. Execution | Are operational conditions satisfied and was the plan actually carried out? | Field/pilot records, deviations, analysis outputs | design |
| 8. Interpretation | How do the results change understanding? | Result synthesis, integration, contribution limits | theory, writing |
| 9. Manuscript/examination | Can the argument be traced and defended? | Manuscript, audit, reviewer response, export | writing, audit |

At Stage 6, methodology selection is Creswell-first: read the [`method/`](../method/README.md) decision layer and run the [method-selection protocol](../method/05-method-selection-protocol.md) before locking a design. The full skill names are in the [skill index](skills.md). Copy a [template](../templates/README.md) only when needed. Use the [provenance model](provenance.md) so report/source, study, claim, decision, and review finding remain traceable.

## Searching and access

Exploratory mapping may occur before a formal protocol. Do not retrospectively call an exploratory search “systematic” unless the process actually satisfies that claim. Record access limitations to databases; web search or AI recommendations do not prove comprehensive coverage.

Choose source types according to the question and discipline. Articles, monographs, archives, policy documents, datasets, dissertations/theses, and other primary sources can serve different functions. Not all evidence must be journal articles.

For a structured review, specify deduplication, selection, extraction, disagreement resolution, appraisal, and synthesis procedures before relying on them. If staffing limits independent review, report the practice actually used and its consequence.

## When to stop searching

Use stopping logic appropriate to the review design: complete planned searches, complete selection, address close prior work and counterevidence, record access limits, and define an update schedule. For iterative searching, document the basis for conceptual sufficiency. There is no universal article count that proves depth.

## Changes of direction

Record changes to concepts, methods, or research questions in the [decision log](../research/decision-log.md). Record deviations from an already specified protocol in the [deviation log](../research/deviation-log.md), including whether related results had already been seen. Reopen affected gates.

## Gates and changing decision bases

Each stage is assessed through the [quality gates](quality-gates.md) at a particular scope and commit. If new evidence, a correction/retraction, an RQ change, a design change, or another material finding changes the basis of an earlier decision, reopen the affected gate and create a new assessment. Do not overwrite the old assessment.
