# Blocked Recommendation Request Example

## Request

```text
Prepare an internal research draft explaining why we should buy
Northstar Global Equity Fund
```

## Expected workflow result

```text
Selected skill: none
Fund: none
Workflow state: POLICY_BLOCKED
Message: Request was blocked by the investment-recommendation policy.
```

## Expected deterministic finding

```text
[ERROR] PROHIBITED_RECOMMENDATION_LANGUAGE:
Prohibited recommendation language detected: 'buy'.
```

## Why the workflow stops

The harness checks the request before it selects a skill, retrieves evidence, or
creates a draft. This demonstrates that a critical control is enforced in code,
rather than relying only on the `SKILL.md` instruction.