# Changelog

All notable changes to Better Research are recorded here. The repository uses semantic versioning for the **builder contract**, not for the maturity of any research project.

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
