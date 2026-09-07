# Changelog

All notable changes to Better Research are recorded here. The repository uses semantic versioning for the **builder contract**, not for the maturity of any research project.

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
