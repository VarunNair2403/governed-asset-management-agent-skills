---
name: fund-research-draft
description: Create an internal-only, non-recommendation fund research draft from approved synthetic evidence. All outputs require human review.
version: 0.1.0
---

# Fund Research Draft

## When to use this skill

Use this skill when a user asks to prepare, draft, summarize, or create an
internal research report or research-preparation document for a synthetic fund.

## Purpose

Create a structured internal research draft from an approved synthetic evidence
package. This skill supports research preparation only and does not provide
investment advice, a recommendation, or a decision.

## Required workflow

1. Confirm the requested fund exists in the approved synthetic data store.
2. Run the evidence-quality check before generating a draft.
3. Continue only if the evidence decision is `SUFFICIENT`.
4. Use approved evidence only.
5. Include all required report sections:
   - Market exposure
   - Allocation
   - Key risks
   - Sources
   - Disclaimer
6. Validate the draft for required sections, approved source references, and
   prohibited recommendation language.
7. Set the final workflow state to `PENDING_HUMAN_REVIEW`.

## Required disclaimer

> Synthetic demonstration data only. This internal research-preparation draft
> is not investment advice, a recommendation, or a solicitation. It must be
> reviewed by an authorized human reviewer before any further use.

## Prohibited actions

- Do not recommend, endorse, rate, approve, or reject a fund.
- Do not use buy, sell, hold, target price, overweight, underweight, or similar
  recommendation language.
- Do not make portfolio-allocation recommendations.
- Do not publish, distribute, email, or otherwise send the draft externally.
- Do not transition the output to an approved, published, or client-ready state.

## Output requirements

Return a structured internal draft containing the required sections and:

```text
workflow_state: PENDING_HUMAN_REVIEW
```