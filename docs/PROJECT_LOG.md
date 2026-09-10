# Project Log

This file is the canonical record of major decisions, completed work,
verification results, and next steps.

---

## MVP v0.1 — Complete

**Date:** 2026-09-09  
**Status:** Complete

### Goal

Build and ship a compact GitHub portfolio prototype that demonstrates governed
Agent Skills for an internal asset-management research-preparation workflow.

### Decisions

- **Repository:** `governed-asset-management-agent-skills`
- **Use case:** Synthetic internal fund-research preparation.
- **Skills:**
  1. `evidence-quality-check`
  2. `fund-research-draft`
- **Runtime:** Local, deterministic, dependency-light, and offline-capable.
- **Data:** Fictional synthetic fund evidence only.
- **Core principle:** `SKILL.md` guides behavior; deterministic Python code
  enforces evidence, content, and workflow controls.
- **Human oversight:** Every valid research draft ends in
  `PENDING_HUMAN_REVIEW`.

### Implemented

- Repository foundation with a `src/` Python package layout.
- Two reusable `SKILL.md` definitions with frontmatter metadata.
- Local skill registry for metadata discovery.
- `list-skills` CLI command.
- Local synthetic evidence store with:
  - Northstar Global Equity Fund: complete approved evidence.
  - Summit Private Credit Fund: intentionally stale and incomplete evidence.
- Deterministic evidence checks for:
  - Package approval.
  - Required evidence fields.
  - Source ID presence.
  - Source approval.
  - Evidence freshness.
- Deterministic request router.
- Governed `fund-research-draft` workflow.
- Deterministic draft validation for:
  - Required report sections.
  - Required disclaimer.
  - Prohibited recommendation terms.
- Mandatory `PENDING_HUMAN_REVIEW` state.
- Five versioned evaluation cases.
- Nine unit and integration tests.
- GitHub Actions CI workflow.
- README architecture diagram and representative examples.

### Verification

```bash
python evals/run_evals.py
```

Result:

```text
Evaluation summary: 5/5 passed
```

```bash
PYTHONPATH=src python -m pytest -q
```

Result:

```text
9 passed
```

### Deliberate boundaries

- No live market, fund, client, or portfolio data.
- No LLM, Azure AI Foundry integration, vector database, or web interface.
- No investment recommendations, trade execution, portfolio construction,
  publishing, or client communication.
- No production-compliance claim.

### Potential v0.2 improvements

1. Optional Azure AI Foundry drafting adapter behind the existing evidence and
   output validators.
2. Structured audit traces.
3. A compliance/provenance review skill.
4. LLM-assisted routing with confidence thresholds and deterministic fallback.
5. Streamlit UI while retaining the CLI.
6. Docker support and dependency lock file.