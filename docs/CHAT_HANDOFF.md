# Chat Handoff

Paste this document into a new AI chat to continue work on the project.

## Project

`governed-asset-management-agent-skills`

A compact Python portfolio prototype demonstrating reusable Agent Skills and a
minimal deterministic harness for synthetic, internal asset-management
research-preparation workflows.

## Current status

MVP v0.1 is complete locally and ready to be pushed to GitHub.

Implemented:

- Two skills:
  - `evidence-quality-check`
  - `fund-research-draft`
- Metadata-based skill registry and `list-skills` CLI command.
- Deterministic request router and controlled synthetic evidence retrieval.
- Evidence approval, completeness, source ID, source approval, and freshness checks.
- Internal research-draft workflow that runs only after sufficient evidence.
- Required-section, disclaimer, and prohibited-language validation.
- Mandatory `PENDING_HUMAN_REVIEW` state.
- Five versioned evaluations and nine passing tests.
- GitHub Actions CI configuration.
- Portfolio-focused README and representative examples.

## Verification

```bash
python evals/run_evals.py
# Evaluation summary: 5/5 passed

PYTHONPATH=src python -m pytest -q
# 9 passed
```

## Non-negotiable boundaries

- Synthetic data only.
- Internal research preparation only.
- No investment advice or recommendations.
- No trade execution, publishing, client communication, or portfolio construction.
- Every valid draft ends in `PENDING_HUMAN_REVIEW`.
- Recommendation language such as `buy`, `sell`, or `hold` is deterministically blocked.

## Immediate next task

Push the local repository to a new GitHub repository, confirm GitHub Actions CI
passes, then add the GitHub Actions status badge to `README.md`.

## Potential future work

- Optional Azure AI Foundry drafting adapter.
- Structured audit traces.
- Compliance/provenance review skill.
- LLM-assisted routing with confidence thresholds.
- Streamlit interface.