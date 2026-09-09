---
name: evidence-quality-check
description: Validate whether a synthetic fund evidence package is complete, approved, and current enough for internal research preparation.
version: 0.1.0
---

# Evidence Quality Check

## When to use this skill

Use this skill when a user asks to check, validate, assess, or confirm the
quality, completeness, approval status, source coverage, or freshness of a
synthetic fund evidence package before internal research preparation.

## Purpose

Determine whether a synthetic evidence package contains the minimum approved
information required to support an internal research-preparation workflow.

## Required checks

1. Confirm the fund exists in the approved synthetic data store.
2. Confirm the fund package is marked `APPROVED_INTERNAL_SYNTHETIC`.
3. Confirm all sources have a source ID and are approved.
4. Confirm required evidence categories are present:
   - Market exposure
   - Allocation
   - Risks
   - Sources
5. Flag evidence that is missing, unapproved, unknown, or stale.
6. Return a structured decision and findings.

## Output requirements

Return one of:

- `SUFFICIENT`
- `INSUFFICIENT`
- `HUMAN_REVIEW_REQUIRED`
- `FUND_NOT_FOUND`

Include a list of findings. Each finding must contain a severity, code, and
human-readable message.

## Constraints

- Use synthetic data only.
- Do not provide investment advice or recommendations.
- Do not infer, fabricate, or repair missing evidence.
- Do not create, publish, or distribute a research report.
- Escalate conflicting or ambiguous evidence for human review.