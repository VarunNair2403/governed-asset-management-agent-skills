# Project Log

This file is the canonical record of major decisions, completed work,
verification results, and next steps.

---

## Milestone 01 — Project foundation

**Date:** 2026-09-08  
**Status:** In progress

### Goal

Create a compact, portfolio-ready Python repository for governed
asset-management Agent Skills.

### Decisions

- **Repository name:** `governed-asset-management-agent-skills`
- **MVP scope:** Two skills, a deterministic local harness, synthetic data,
  deterministic validators, five evaluation cases, tests, and GitHub Actions CI.
- **Core skills:**
  1. `evidence-quality-check`
  2. `fund-research-draft`
- **Primary workflow:** A user requests an internal fund research draft; the
  system retrieves controlled synthetic evidence, validates it, creates a
  structured internal draft, validates the output, and routes the result to
  `PENDING_HUMAN_REVIEW`.
- **Data boundary:** Synthetic data only.
- **Control principle:** `SKILL.md` guides agent behavior; deterministic Python
  enforces evidence, content, and workflow controls.
- **Runtime boundary:** The MVP is offline-capable and does not require an LLM,
  Azure AI Foundry, a vector database, or a web UI.

### Non-negotiable boundaries

- No investment recommendations or advice.
- No buy, sell, hold, target-price, overweight, or underweight language.
- No trade execution, portfolio construction, automatic publishing, client
  communication, or external distribution.
- All valid internal research drafts end in `PENDING_HUMAN_REVIEW`.

### Implemented

- Repository initialized.
- Base directory structure created.
- Python packaging configuration added.
- Initial README, license, Git ignore rules, and continuity documents added.

### Verification

Pending initial file review and Git commit.

### Next milestone

Create the shared data models, two `SKILL.md` definitions, and a minimal
metadata-based skill registry.