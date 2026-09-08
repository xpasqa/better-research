# Changelog

All notable changes to Better Research are recorded here. The repository uses semantic versioning for the **builder contract**, not for the maturity of any research project.

## [0.2.0] - 2026-09-08

Creswell-first methodological decision layer.

### Added

- New `method/` knowledge layer grounded in Creswell & Creswell (2023).
- Explicit research-design flow from research problem and questions to worldview, approach, design, methods, and method-chapter drafting.
- Detailed qualitative, quantitative, and mixed-methods design guidance.
- AI method-selection protocol with human approval checkpoints and falsification checks.
- Practical method-chapter blueprint and method-input contracts.

### Changed

- `AGENTS.md` now requires the Creswell-first method layer before substantive methodology recommendations.
- `research-design` now uses Creswell & Creswell as the default research-design architecture while retaining specialist sources for technical methods.
- Research workflow, skill index, standards register, repository map, and project brief now reference the methodology layer.
- Builder version bumped to 0.2.0.

### Migration

Projects on 0.1.1 should follow [0.1.1 → 0.2.0](docs/migrations/0.1.1-to-0.2.0.md). Migration adds a methodological decision framework; it does not automatically invalidate or rewrite an already approved research design.

## [0.1.1] - 2026-09-07

Global-English documentation and multilingual research-output policy.

### Changed

- Repository documentation, skills, templates, examples, and project scaffolding are now written in English for global portability.
- Canonical placeholder/status tokens are now English: `NOT YET FILLED`, `NOT YET DECIDED`, `NOT YET VERIFIED`, `NOT ASSESSED`, `REVISION REQUIRED`, `READY`, and `NOT APPLICABLE`.
- The project brief now treats research-output language as a project-level decision rather than assuming Indonesian.
- `research-writing` and manuscript guidance explicitly support Indonesian, English, bilingual, and multilingual research outputs.
- The bootstrap script now targets the English project-brief schema.

### Migration

Projects on 0.1.0 should follow [0.1.0 → 0.1.1](docs/migrations/0.1.0-to-0.1.1.md). Existing research projects should not translate active empirical content merely to match the builder; the migration concerns builder instructions, scaffolding, and status vocabulary.

## [0.1.0] - 2026-09-07

First explicitly versioned builder baseline.

### Added

- Epistemic bounded-context Issue schema.
- Pull Request epistemic delta and layered verification.
- Mechanical repository-integrity checks in GitHub Actions.
- Formal SRC/STUDY/CLM/DEC/REV provenance model.
- Bibliographic identity and report–study lifecycle rules.
- Synthetic golden end-to-end research example.
- Diagnostic quality-gate structure and reopen rules.
- Cross-agent adapter files that redirect to the canonical `AGENTS.md`.
- Explicit MIT license and upstream attribution.
- Builder version and migration policy.

### Changed

- Local skills use the `research-*` namespace.
- `research-rigor` applies Karpathy-inspired execution discipline to research.
- README centers recoverable, bounded-context research rather than chat memory.

### Migration

Projects copied before versioning should follow [unversioned → 0.1.0](docs/migrations/unversioned-to-0.1.0.md). Existing research projects do **not** automatically inherit this version.
