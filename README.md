# Better Research

Builder version: **0.2.0** · [Changelog](CHANGELOG.md) · [Migration policy](docs/migrations/README.md) · [MIT License](LICENSE)

> **Do not ask AI to remember your entire research project. Build a system that makes research context recoverable.**

**Better Research** is a Git-based research workspace for designing, conducting, writing, and auditing research with AI without treating chat history as the project’s memory.

AI context is finite. Serious research is not. A research project can span months or years and accumulate hundreds of sources, decisions, revisions, analyses, reviews, and changes of direction. If that state lives only inside conversations, some of it will eventually be lost, mixed together, or reconstructed incorrectly.

Better Research externalizes research memory into an auditable workflow:

```text
Research question / problem
        ↓
GitHub Issue
(bounded context + success criteria)
        ↓
Branch
(one scoped unit of work)
        ↓
Evidence / analysis / writing
        ↓
Pull Request
(diff + verification + review)
        ↓
Merge into main
        ↓
Checkpoint + academic quality gate
```

**Chat is temporary. Issues preserve working context. Files preserve research knowledge. Git preserves change. Pull Requests integrate results.**

This repository is the reusable **builder/template**. Initial state: **ready to use; no substantive research has started**.

---

## Why Better Research exists

The main failure mode of AI-assisted research is not only hallucination. A more systemic risk is **context drift**.

Across a long project, an AI agent may:

- forget decisions from earlier sessions;
- mix evidence from different sources or versions;
- change theories, variables, methods, or terminology without tracking consequences;
- strengthen a claim because it sounds plausible rather than because evidence supports it;
- add unnecessary conceptual or methodological complexity;
- rewrite large sections when only one argument needs revision;
- declare work “complete” when evidence, review, ethics, or academic readiness remain unresolved.

Better Research does not try to fix this with an endlessly growing prompt.

It changes the **architecture of the work**.

One task has one bounded context. One substantive change has one reason. One claim has a traceable evidence path. One decision has a history. One output enters `main` only after it can be inspected.

---

# Language policy

The **repository itself is written in English** so researchers and AI systems globally can use the same builder.

The **research output does not have to be in English**.

A project may produce:

- an Indonesian dissertation or thesis;
- an English journal article;
- bilingual reports;
- multilingual source notes or field materials;
- different languages for different audiences or outputs.

Record the project’s language requirements in [`research/project-brief.md`](research/project-brief.md).

Translation must preserve:

- claim strength;
- uncertainty;
- technical meaning;
- quotations;
- attribution;
- the distinction between source content and researcher interpretation.

Repository language and research-output language are separate decisions.

---

# Creswell-first methodology layer

Better Research uses **Creswell & Creswell (2023)** as the default research-design framework for methodological reasoning.

The AI should not jump from a topic directly to a technique. Methodological reasoning starts from the research problem and questions, then makes the relationship among worldview, research approach, research design, and specific methods explicit.

```text
Research problem
        ↓
Purpose / research questions
        ↓
Philosophical worldview
        ↓
Qualitative / Quantitative / Mixed Methods
        ↓
Research design
        ↓
Sampling + data collection + analysis
        ↓
Validity / validation / integration
        ↓
Method chapter
```

The operational decision layer lives in [`method/`](method/README.md). Before recommending a design, read the [Creswell research-design flow](method/01-creswell-research-design-flow.md), run the [method-selection protocol](method/05-method-selection-protocol.md), and then read the relevant qualitative, quantitative, or mixed-methods file.

This is **Creswell-first, not Creswell-only**. Creswell provides the study architecture; specialist methodological literature is still required for technical decisions such as SEM, psychometrics, multilevel models, advanced causal inference, or design-specific qualitative analysis.

AI recommendations remain proposals. Final methodological judgment belongs to the researcher.

---

# Core principles

## 1. An Issue is a bounded context

Every substantive task in a **RESEARCH** workspace starts from a GitHub Issue.

A good Issue preserves:

- objective;
- current epistemic state;
- scope and out-of-scope boundaries;
- evidence required;
- success criteria;
- verification plan;
- decisions;
- blockers and dependencies;
- checkpoints;
- related branch, commit, and PR.

The agent should not load the entire project into one context window. It should load the active Issue and only the artifacts required for that unit of work.

## 2. Files are the canonical research record

Research does not live in chat.

Canonical artifacts live in files:

- framing, decisions, and project state in `research/`;
- literature and evidence trails in `literature/`;
- analysis in `analysis/`;
- manuscript source in `manuscript/`;
- audits and reviews in `reviews/`.

Markdown is preferred because it is readable by humans and AI, diff-friendly, portable, and easy to transform into Word, PDF, LaTeX, or other formats.

## 3. Pull Requests are the integration mechanism

Changes should not disappear directly into a final document.

Work happens on a branch and is integrated through a Pull Request. The PR records:

- what changed;
- why it changed;
- which Issue it addresses;
- which evidence was inspected;
- what epistemic state changed;
- which success criteria passed;
- what remains unknown or blocked;
- what verification was actually performed.

This keeps changes small, reviewable, and coherent.

## 4. Evidence outranks fluent prose

A polished academic sentence is not evidence.

Better Research distinguishes:

- **KNOWN** — actually provided or observed;
- **SUPPORTED** — supported by evidence that was inspected;
- **INFERRED** — concluded from evidence, with reasoning and limits;
- **ASSUMED** — temporarily assumed but not verified;
- **UNKNOWN** — not yet known or accessible;
- **DECISION NEEDED** — requires researcher judgment, more evidence, or authorization.

When evidence is insufficient, the correct state is `UNVERIFIED` or `BLOCKED`, not more confident prose.

---

# Quick Start

## Prerequisites

You should understand at least:

- basic Git and GitHub;
- branches, commits, Issues, and Pull Requests;
- Markdown;
- how to verify academic sources independently.

Better Research does not replace methodological expertise, researcher judgment, supervisors, peer reviewers, ethics committees, or institutional rules.

---

## 1. Create one repository per research project

Do not run multiple substantive projects in one workspace.

### Option A — GitHub Template

If this repository is configured as a GitHub Template Repository, select **Use this template** and create a new private repository.

Then:

1. confirm `.agents/` and `.github/` were copied;
2. switch the project brief to RESEARCH mode;
3. preserve the builder version;
4. create the initialization Issue before substantive customization.

### Option B — cross-platform bootstrap

From a local clone of Better Research:

```bash
python scripts/init_research.py ../my-research --name "My Research Project"
```

Optionally configure the remote:

```bash
python scripts/init_research.py ../my-research \
  --name "My Research Project" \
  --remote git@github.com:OWNER/REPO.git
```

The script:

- copies the builder without upstream `.git/` history;
- switches the copied workspace to RESEARCH mode;
- records the project name;
- initializes a fresh Git repository;
- does not push automatically.

See [creating a research repository](docs/template-repository.md).

A private repository does **not** make participant data, identity keys, signed consent forms, or restricted materials safe to store in Git.

---

## 2. Switch to RESEARCH mode

Open [`research/project-brief.md`](research/project-brief.md).

Change:

```text
Workspace mode: TEMPLATE
```

to:

```text
Workspace mode: RESEARCH
```

| Mode | Purpose | Workflow rule |
|---|---|---|
| `TEMPLATE` | Maintain the upstream Better Research builder | Direct maintenance is allowed when explicitly authorized |
| `RESEARCH` | Conduct an actual research project | Issue + Branch + PR are required for substantive work |

Do not switch modes merely to bypass the research workflow.

---

## 3. Start the first AI session

Give the agent:

> Read AGENTS.md, research/project-brief.md, research/status.md, and docs/skills.md. Verify the owner/repository and confirm the workspace is in RESEARCH mode. Use research-workflow to find or create the project-brief initialization Issue, then use research-framing. Start only from information and sources that are actually available. Do not choose a method, theory, variable, or novelty claim without evidence. Record unknowns, decisions, evidence requirements, success criteria, verification, and checkpoints in the Issue. Route every file change through a branch and Pull Request.

Then complete the project brief incrementally.

You do **not** need a final title, final method, final theoretical model, or final manuscript language before starting.

Leave unresolved fields as:

```text
NOT YET FILLED
NOT YET DECIDED
NOT YET VERIFIED
```

Visible uncertainty is better than premature certainty.

---

# Day-to-day workflow

Do not start with:

> “AI, continue my dissertation.”

Start with a reviewable research task:

> “Does the theoretical-gap argument in section X actually follow from the sources we have inspected?”

Then use:

```text
1. Find or create the Issue
2. Define the objective
3. Record the epistemic state
4. Define scope
5. Define evidence required
6. Define success criteria
7. Define verification
8. Create or continue the branch
9. Make the minimum justified change
10. Verify
11. Save a checkpoint
12. Open or update the PR
13. Review
14. Merge
15. Verify main
16. Close the Issue only when closure conditions are satisfied
```

See the full [Git workflow](docs/git-workflow.md).

---

# Example of a bounded research Issue

```markdown
## Objective

Determine whether institutional trust should remain
as a moderator of the X → Y relationship.

## Epistemic state

### KNOWN
- RQ2 currently specifies moderation.
- Three sources discuss institutional trust.

### SUPPORTED
- No moderation mechanism has yet been verified.

### UNKNOWN
- Whether the closest prior studies already test the same mechanism.
- Whether moderation is theoretically necessary.
- Whether the design can identify moderation.

## Scope

Included:
- theory memo;
- relevant source notes;
- claim ledger;
- directly affected manuscript paragraphs.

Out of scope:
- redesigning the entire methodology;
- adding unrelated constructs;
- rewriting other chapters.

## Success criteria

- [ ] Construct definition verified.
- [ ] Closest prior studies compared.
- [ ] Counterevidence inspected.
- [ ] Alternative explanations inspected.
- [ ] Retain / narrow / defer / reject decision recorded.
```

The canonical Issue template is [`.github/ISSUE_TEMPLATE/research-task.md`](.github/ISSUE_TEMPLATE/research-task.md).

---

# Eight local skills

Skills live under [`.agents/skills/`](.agents/skills/) and are indexed in [`docs/skills.md`](docs/skills.md).

| Skill | Purpose |
|---|---|
| `research-workflow` | Issues, checkpoints, branches, PRs, review, merge, and cross-session recovery |
| `research-rigor` | Cross-stage guardrails for uncertainty, parsimony, scope, falsification, and verification |
| `research-framing` | Problem framing, research questions, boundaries, and feasibility |
| `research-evidence` | Search, screening, extraction, appraisal, source notes, and claim evidence |
| `research-theory` | Theory synthesis, mechanisms, closest studies, alternatives, and contribution testing |
| `research-design` | Alignment of questions, data, design, analysis, ethics, and inference |
| `research-writing` | Evidence-based drafting/revision and manuscript consistency |
| `research-audit` | Quality-gate audit, consistency checks, and examination/review preparation |

Example:

```text
Use research-evidence to verify whether CLM-014 is actually
supported by the available source notes.
```

In environments that support direct skill invocation:

```text
$research-evidence
```

Do not load every skill at once. Use only what the active task requires.

---

# Research Rigor: preventing confident failure

`research-rigor` adapts execution ideas from [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) to research.

## Think Before Claiming

Do not silently convert uncertainty into certainty.

```text
few search results
        ↓
"This is the research gap"
```

is not valid reasoning.

A defensible process is:

```text
few search results
        ↓
check query design, databases, synonyms,
adjacent literature, citation chasing,
and access limitations
        ↓
decide what can actually be claimed
```

## Parsimony First

Complexity is not quality.

Do not automatically build:

```text
3 theories + 8 constructs + 4 mediators + 2 moderators + SEM
```

when a simpler model or design can answer the question more defensibly.

## Surgical Changes

Every substantive change should trace to:

- the Issue;
- evidence;
- a decision;
- a review finding;
- a success criterion.

Do not rewrite unrelated sections merely because an agent sees an opportunity to “improve” them.

## Goal-Driven Research

Replace vague instructions such as:

> “Improve the literature review.”

with inspectable goals:

```text
Objective:
Determine whether the literature review establishes
a defensible unresolved theoretical problem.

Success criteria:
[ ] Core constructs are defined.
[ ] Closest prior studies are compared.
[ ] Counterevidence is represented.
[ ] Major claims are traceable to sources.
[ ] Unsupported claims are removed or flagged.
[ ] The gap is stated without novelty inflation.
```

## Falsification Before Affirmation

For important claims:

```text
candidate claim
   ↓
supporting evidence
   ↓
contradictory evidence
   ↓
alternative explanations
   ↓
boundary conditions
   ↓
claim strength
```

Do not search only for confirmation.

---

# Academic workflow

Better Research uses a Creswell-first framework for selecting research methodology, but it does not preselect qualitative, quantitative, mixed methods, or a specific design before the research problem and questions justify that choice.

| Stage | Main decision question | Typical artifact |
|---|---|---|
| Context | What are the mandate, constraints, resources, and uncertainties? | Project brief |
| Framing | What knowledge problem is actually researchable? | Problem memo, RQ |
| Mapping | Which concepts and debates matter? | Literature map |
| Protocol | How will evidence be searched and evaluated transparently? | Review protocol |
| Evidence | What do inspected sources actually report? | Search log, screening, source notes, claim ledger |
| Theory | Which explanations survive comparison and counterevidence? | Theory/contribution memo |
| Design | What evidence is required to answer the RQ? | Design matrix, analysis plan, ethics/data plan |
| Execution | Were authorized activities actually carried out as planned? | Execution/analysis trail, deviation log |
| Interpretation | What do results mean, and what are the inferential limits? | Result synthesis |
| Writing & Audit | Can the argument be traced and defended? | Manuscript, review, export |

See [`docs/research-workflow.md`](docs/research-workflow.md).

Stages may repeat when evidence changes an earlier decision.

---

# Quality Gates G0–G7

A complete set of files does not mean the research is academically ready.

```text
Delivery status
Issue / PR complete
        ≠
Academic readiness
Quality gate READY
```

| Gate | Assesses |
|---|---|
| G0 | Context and research mandate |
| G1 | Problem and research questions |
| G2 | Literature protocol and evidence |
| G3 | Theory and contribution |
| G4 | Research design |
| G5 | Execution readiness |
| G6 | Results and interpretation |
| G7 | Manuscript and examination/review readiness |

Statuses:

- `NOT ASSESSED`
- `REVISION REQUIRED`
- `READY`
- `NOT APPLICABLE`

Full criteria: [`docs/quality-gates.md`](docs/quality-gates.md).

An agent’s assessment is not supervisor approval, ethics approval, peer review, or institutional approval.

---

# Literature, citations, and reference managers

Canonical bibliographic metadata lives in:

[`literature/references.bib`](literature/references.bib)

The file starts empty so the builder does not ship fictional references.

Recommended flow:

```text
Search
  ↓
Screening
  ↓
Read original source
  ↓
Source note
  ↓
Verified metadata
  ↓
references.bib
  ↓
Claim ledger
  ↓
Manuscript citation
```

Markdown manuscripts may use citation keys such as:

```markdown
... as discussed in prior literature [@citation-key].
```

`references.bib` can be exchanged with reference managers such as Zotero or Mendeley. Avoid manually maintaining the same bibliographic metadata in several places.

Licensed PDFs should remain in approved local/institutional storage. Do not commit copyrighted PDFs or sensitive data merely because the repository is private.

See [`literature/README.md`](literature/README.md) and [`manuscript/README.md`](manuscript/README.md).

---

# Provenance: source → study → claim → decision

Better Research uses stable local identifiers:

```text
SRC (report/source)
   ↓ reports / derives from
STUDY
   ↓ supports / contradicts / limits
CLM (claim)
   ↓ informs / challenges
DEC (decision)
   ↓ changes
RQ / protocol / design / manuscript / gate

REV (review finding) can challenge a CLM, DEC, or artifact.
```

Claims can be:

`DRAFT` / `UNVERIFIED` / `SUPPORTED` / `MIXED` / `CONTRADICTED` / `RETRACTED`.

Evidence relations can be:

`SUPPORTS` / `CONTRADICTS` / `LIMITS` / `CONTEXTUALIZES`.

See [`docs/provenance.md`](docs/provenance.md).

---

# Markdown as the canonical source

Better Research prioritizes Markdown because it is:

- readable by humans and AI;
- easy to review with Git diff;
- suitable for surgical paragraph-level changes;
- independent of one application;
- easy to convert into other formats;
- easy to connect to evidence and provenance.

Word, PDF, LaTeX, or institution-specific documents should be treated as exports unless the project explicitly decides otherwise.

---

# Automated repository checks

GitHub Actions performs mechanical checks on Pull Requests and pushes to `main`:

- relative Markdown links;
- skill frontmatter and names;
- stale legacy skill identifiers;
- basic `references.bib` structure and duplicate citation keys;
- prohibited sensitive/private paths;

Run locally:

```bash
python scripts/validate_repository.py
```

A PASS means **mechanical repository integrity**. It does not mean the claims are valid, the method is appropriate, or an academic quality gate is READY.

Workflow: [`.github/workflows/repository-integrity.yml`](.github/workflows/repository-integrity.yml).

---

# Repository map

```text
.
├── AGENTS.md
├── .agents/
│   └── skills/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── pull_request_template.md
├── .cursor/
├── CLAUDE.md
├── VERSION
├── CHANGELOG.md
├── scripts/
├── examples/
├── research/
├── method/
├── literature/
├── analysis/
├── manuscript/
├── data/
├── reviews/
├── exports/
├── templates/
└── docs/
```

| Location | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Canonical agent rules |
| [`.agents/skills/`](.agents/skills/) | Eight research skills |
| [`research/`](research/project-brief.md) | Project brief, status, decisions, deviations, and AI-use log |
| [`method/`](method/README.md) | Creswell-first methodology selection, design logic, AI rules, and method-chapter blueprint |
| [`literature/`](literature/README.md) | Search trail, screening, source notes, claim ledger, and bibliography |
| [`analysis/`](analysis/README.md) | Analysis plan and analysis trail |
| [`manuscript/`](manuscript/README.md) | Canonical manuscript guidance |
| [`data/`](data/README.md) | Data-governance guidance |
| [`reviews/`](reviews/README.md) | Audits, reviews, and responses |
| [`exports/`](exports/README.md) | Export outputs and checks |
| [`templates/`](templates/README.md) | Working research forms |
| [`docs/`](docs/research-workflow.md) | Workflow, provenance, standards, integrity, Git, Issues, PRs, and migrations |
| [`scripts/`](scripts/) | Bootstrap and mechanical validation |
| [`examples/`](examples/toy-research/) | Synthetic end-to-end example |
| [`VERSION`](VERSION) / [`CHANGELOG.md`](CHANGELOG.md) | Builder version and history |
| [`LICENSE`](LICENSE) / [`NOTICE.md`](NOTICE.md) | License and attribution |

---

# Available templates

Better Research includes:

- session checkpoint;
- problem memo;
- review protocol;
- search log;
- screening log;
- source note;
- claim ledger;
- theory/contribution audit;
- design matrix;
- analysis plan;
- ethics/data plan;
- chapter/section plan;
- gate review;
- review response.

See [`templates/README.md`](templates/README.md).

Create a working template only when the project reaches the stage that needs it.

---

# Versioning and migration

Every research repository **pins the builder version** from which it was created.

A research project does not silently inherit later Better Research changes.

```text
research project vX
        ↓
upstream builder changes
        ↓
NO automatic sync
        ↓
read migration notes
        ↓
migration Issue
        ↓
branch + verification + PR
        ↓
project builder version updated
```

This protects reproducibility: research rules, skill behavior, provenance schema, and quality gates should not change invisibly in the middle of a project.

See [`VERSION`](VERSION), [`CHANGELOG.md`](CHANGELOG.md), and [migration policy](docs/migrations/README.md).

---

# Portability across AI agents

`AGENTS.md` is the **single canonical instruction source**.

Thin adapters exist for environments that recognize different files:

- `CLAUDE.md` — Claude Code;
- `.cursor/rules/better-research.mdc` — Cursor;
- `.github/copilot-instructions.md` — GitHub Copilot;
- environments supporting `AGENTS.md` read it directly.

Adapters must not become independent copies of the research rules.

---

# Golden example

[`examples/toy-research/`](examples/toy-research/) demonstrates a fully synthetic cycle:

```text
Issue
  ↓
source provenance
  ↓
claim ledger
  ↓
decision
  ↓
surgical manuscript change
  ↓
verification
  ↓
gate review
```

Everything in the example is labeled **SYNTHETIC EXAMPLE** and must not be treated as academic evidence.

---

# Continuing in a future AI session

You should not need to ask:

> “Do you remember what we discussed last week?”

Use the Issue.

Example continuation instruction:

> Read AGENTS.md and continue Issue #[number] in [owner/repo]. Read the current snapshot, latest checkpoint, decisions, dependencies, linked SRC/CLM records, PRs, and open review findings. Reconcile them with the actual branch/commit state. Summarize the current position, state remaining unknowns or blockers, and continue only work that has not yet satisfied the success criteria. Save a checkpoint before the session ends.

The project should be recoverable from the repository, not from chat memory.

---

# When to create a new Issue

Create a new Issue when there is an **independently reviewable decision or output**.

Good:

```text
#31 Verify theoretical mechanism for RQ2
#32 Audit measurement validity for construct X
#33 Revise discussion against contradictory findings
```

Bad:

```text
#31 Do my dissertation
#32 Continue the research
#33 Make it better
```

Clarifying questions within an active task remain on the active Issue.

Large stages can use a parent Issue plus child Issues.

---

# Definition of done

A file-producing task is complete for **delivery** when:

- applicable Issue success criteria are PASS;
- changes exist on the correct branch;
- actual checks are recorded;
- the PR was reviewed;
- the PR is merged into `main`;
- the resulting `main` commit was verified;
- the Issue closure matches the evidence.

But:

```text
MERGED ≠ scientifically valid
MERGED ≠ ethics approval
MERGED ≠ supervisor approval
MERGED ≠ research completed
```

Academic quality remains an evidence, method, review, and quality-gate decision.

---

# Non-negotiable rules

1. Do not fabricate sources, DOI values, quotations, pages, data, results, permissions, approvals, or research activities.
2. Do not state that a source supports a claim before checking the support.
3. Do not select a method merely because it is popular or sophisticated.
4. Do not hide contradictory evidence.
5. Do not describe two AI agents/runs as two independent human reviewers.
6. Do not store sensitive participant data in Git.
7. Do not claim ethics approval, pilot work, fieldwork, analysis, or human review that did not occur.
8. Do not treat citation count, manuscript length, statistical significance, or low text similarity as proof of quality.
9. Do not perform broad unrelated rewrites when only a narrow change is required.
10. Do not use chat history as the only source of project decisions.

See [`docs/academic-integrity.md`](docs/academic-integrity.md).

---

# What Better Research does not do

Better Research is a **research operating system**, not a truth machine.

It does not automatically:

- provide access to Scopus, Web of Science, ProQuest, or paid databases;
- read sources that were not provided or accessible;
- turn AI into a human reviewer;
- issue ethics approval;
- choose the correct design without project information;
- prove novelty from a short search;
- run valid statistical analysis without suitable data and assumptions;
- guarantee journal acceptance or examination success;
- replace researcher, supervisor, reviewer, or institutional judgment.

A strong workflow reduces avoidable failure. It does not remove the need for research judgment.

---

# Philosophy

Large research projects should not depend on one AI session remembering everything.

Build a system where:

```text
every important claim has evidence,
every decision has a reason,
every change has a diff,
every task has a scope,
every session has a checkpoint,
and every contribution can be defended.
```

**Better Research does not try to make AI remember the entire project.  
It makes the project recoverable, inspectable, and continuable.**

---

## Key documentation

- [Agent rules](AGENTS.md)
- [Research workflow](docs/research-workflow.md)
- [Creswell-first methodology layer](method/README.md)
- [Method selection protocol](method/05-method-selection-protocol.md)
- [Git workflow](docs/git-workflow.md)
- [Issue guidance](docs/issues.md)
- [Session continuity](docs/session-continuity.md)
- [Pull Requests and merge](docs/pull-requests.md)
- [Quality gates](docs/quality-gates.md)
- [Academic integrity](docs/academic-integrity.md)
- [Skill index](docs/skills.md)
- [Standards register](docs/standards.md)
- [Provenance model](docs/provenance.md)
- [Migration policy](docs/migrations/README.md)
- [Golden example](examples/toy-research/)
- [Attribution and notices](NOTICE.md)
