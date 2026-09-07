---
name: research-workflow
description: Manage required Issues, cross-session checkpoints, branches, PRs, reviews, and closure so research context remains recoverable.
---

# Work and Context Coordination

Use this skill when starting or continuing project work, saving a handoff, or preparing an output for integration. Read the [Git workflow](../../../docs/git-workflow.md) and the relevant guidance for [Issues](../../../docs/issues.md), [session continuity](../../../docs/session-continuity.md), or [Pull Requests](../../../docs/pull-requests.md).

Check the workspace mode in the project brief first. User-authorized maintenance of the upstream TEMPLATE repository may be inspected and saved directly without an Issue/PR. For a copied project, switch to RESEARCH during provisioning; all Issue/PR requirements below then apply. Do not change modes to bypass the research workflow.

## Invariants

- Select or create an Issue before substantive work. Do not create duplicate Issues for continuation of the same task.
- Verify the Git origin and canonical GitHub repository name; use explicit owner/repo identifiers for external operations and do not accidentally write to the upstream builder.
- All file changes entering `main` in RESEARCH mode go through a branch and PR.
- The Issue preserves delivery context; canonical artifacts remain in files. Keep the current state concise and link to detailed artifacts so a long Issue does not consume the entire context window.
- Review and merge must actually occur under the applicable authorization and repository protections. Do not claim final integration merely because a branch was pushed.

## Workflow

1. Read the Issue, latest checkpoint, decisions, linked PR/review, and actual Git state; reconcile discrepancies before continuing.
2. Define scope, acceptance criteria, dependencies, branch, and the academic skill required. Record uncertainty before making a decision that depends on it.
3. Perform the authorized work; save a [checkpoint](../../../templates/session-checkpoint.md) at the end of the session, after a major decision change, when blocked, and during review transitions.
4. Prepare a draft PR with evidence and limitations. Use `Refs` for partial work; use `Closes` only when the entire Issue is satisfied.
5. Inspect outputs and review findings; merge only within the authorization that actually applies.
6. Verify that the PR is merged, the resulting commit is in `main`, and the Issue state/closure comment matches reality. Keep delivery completion separate from academic readiness.

If GitHub is unavailable, store a local checkpoint marked **NOT YET SYNCED** and report the limitation. Do not pretend that an Issue or PR exists. Clarifying/status questions belong to the active Issue; reading/review tasks that produce project decisions should create an integrated memo through the normal workflow.

## Execution discipline

Apply the cross-skill principles in `research-rigor`: do not silently resolve uncertainty, use the minimum sufficient complexity, keep changes within task scope, and verify outcomes against explicit acceptance criteria. For high-impact claims or decisions, inspect counterevidence and alternative explanations before strengthening the conclusion.

## Provenance and versioning

For work that changes claims or decisions, use the [provenance model](../../../docs/provenance.md). A RESEARCH project pins its builder version in the project brief; upgrade rules, skills, or templates only through an explicit migration Issue + PR, never through silent upstream synchronization.
