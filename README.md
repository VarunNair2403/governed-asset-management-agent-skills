# Governed Asset Management Agent Skills

A compact Python prototype demonstrating how reusable Agent Skills and a
minimal agent harness can support safe, internal fund-research preparation.

The project uses **synthetic data only**. It is designed as a portfolio
reference implementation, not a production investment-advice, trading,
portfolio-management, or client-communications system.

## What it demonstrates

- Reusable Agent Skills packaged as folders centered on `SKILL.md`
- Progressive skill discovery: metadata first, detailed instructions only when selected
- A lightweight, deterministic skill router
- Controlled synthetic evidence retrieval
- Deterministic validation for evidence completeness, approved sources,
  required report sections, and prohibited recommendation language
- Mandatory `PENDING_HUMAN_REVIEW` workflow state for valid research drafts
- Versioned evaluation cases, unit tests, and GitHub Actions CI

## MVP workflow

```text
User request
  -> Skill discovery
  -> Deterministic routing
  -> Synthetic evidence retrieval
  -> Evidence validation
  -> Internal research-draft generation
  -> Output validation
  -> PENDING_HUMAN_REVIEW
```

## Skills

| Skill | Purpose |
|---|---|
| `evidence-quality-check` | Determine whether synthetic fund evidence is complete, approved, and current enough for internal research preparation |
| `fund-research-draft` | Create a structured, internal-only research draft from approved synthetic evidence and route it to human review |

## Safety and governance boundaries

This repository:

- Uses fictional funds and synthetic evidence only
- Supports internal research preparation, not investment decision-making
- Does not provide investment advice or recommendations
- Prohibits terms such as buy, sell, hold, target price, overweight, and underweight
- Does not execute trades, construct portfolios, publish reports, or send client communications
- Requires human review for every otherwise-valid research draft
- Demonstrates controls through deterministic Python validation, not Markdown instructions alone

## Project status

In active development. The initial MVP will include a CLI, two skills, local
synthetic data, validators, five evaluation cases, unit tests, and GitHub
Actions CI.

## License

MIT. See [LICENSE](LICENSE).