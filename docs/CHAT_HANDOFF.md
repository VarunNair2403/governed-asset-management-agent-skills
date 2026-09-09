# Chat Handoff

Use this document when continuing the project in a new AI chat.

## Project

`governed-asset-management-agent-skills`

A compact Python portfolio prototype that demonstrates reusable Agent Skills,
a minimal governed agent harness, synthetic evidence, deterministic validation,
human-review routing, evaluations, tests, and CI.

## MVP scope

- Two skills:
  - `evidence-quality-check`
  - `fund-research-draft`
- Local CLI
- Metadata-based skill discovery and deterministic routing
- Two fictional synthetic funds
- Evidence, source, required-section, prohibited-language, and workflow-state checks
- Five versioned evaluation cases
- Unit tests and GitHub Actions CI

## Core architecture principle

`SKILL.md` guides behavior. Python code enforces controls. Human reviewers
retain decision authority.

## Non-negotiable boundaries

- Synthetic data only
- Internal research preparation only
- No investment advice or recommendations
- No trading, publishing, client distribution, or portfolio construction
- Every valid draft ends in `PENDING_HUMAN_REVIEW`
- Unsafe recommendation requests must be deterministically blocked

## Current status

Milestone 01: Project foundation is being created.

## Next task

Create:
1. Shared Python data models
2. The two `SKILL.md` files
3. A minimal registry that discovers skill metadata from `skills/*/SKILL.md`

Keep the implementation intentionally small, offline-capable, and easy to
explain in a GitHub portfolio review.