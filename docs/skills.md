# Local Skill Index

Open this repository in an AI development/research environment that can read project files. Skills are stored with the builder; no global installation is required. If automatic skill discovery is unavailable, open the linked SKILL.md manually and follow it.

| Skill | Use when | Typical output |
|---|---|---|
| [research-workflow](../.agents/skills/research-workflow/SKILL.md) | Starting/continuing an Issue, preserving context, preparing a PR, or closing work | Issue, checkpoint, branch/PR, integration trail |
| [research-rigor](../.agents/skills/research-rigor/SKILL.md) | Applying cross-stage guardrails for assumptions, parsimony, scope, falsification, and verification | Success criteria, scope boundaries, pass/blocked status, decision trail |
| [research-framing](../.agents/skills/research-framing/SKILL.md) | Clarifying the problem, questions, scope, or feasibility | Project brief/problem memo with explicit open decisions |
| [research-evidence](../.agents/skills/research-evidence/SKILL.md) | Designing or conducting search, screening, extraction, or appraisal | Protocol, logs, source notes, claim ledger |
| [research-theory](../.agents/skills/research-theory/SKILL.md) | Synthesizing debates and testing contribution candidates | Argument map, alternative explanations, novelty/contribution audit |
| [research-design](../.agents/skills/research-design/SKILL.md) | Selecting design, measurement, analysis, and execution requirements | Design matrix, analysis plan, ethics/data plan |
| [research-writing](../.agents/skills/research-writing/SKILL.md) | Drafting or revising an evidence-based manuscript | Manuscript with citations and explicit claim limits |
| [research-audit](../.agents/skills/research-audit/SKILL.md) | Assessing quality, readiness, or examination preparation | Location/evidence-based review and follow-up actions |

A skill may be invoked by name, for example `$research-evidence`, when the environment supports it. A skill does not search databases or assess a manuscript merely by existing in the repository; it must be used within an actual task.

## Combining skills and respecting limits

Use `research-workflow` for coordination, apply `research-rigor` as the cross-stage execution discipline, and select the academic skill that matches the required output. A typical academic flow is framing → evidence → theory → design → writing → audit, with iteration when evidence changes earlier decisions.

Do not load every skill at once. Read only what the active task requires.

Environment-specific document/PDF/spreadsheet capabilities may be used for artifacts that require them. Deep-research or scholarly connectors, when available and explicitly appropriate, may extend access; their outputs still require project-level verification and appraisal.

If a tool or source is unavailable, report the access limit and continue only the parts that can be performed honestly. Never claim a Scopus, Web of Science, ProQuest, or other database search that did not actually occur.
