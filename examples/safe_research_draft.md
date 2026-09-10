# Safe Internal Research Draft Example

## Request

```text
Prepare an internal research draft for Northstar Global Equity Fund
```

## Expected workflow result

```text
Selected skill: fund-research-draft
Fund: Northstar Global Equity Fund
Workflow state: PENDING_HUMAN_REVIEW
Message: Internal research draft created and routed to human review.
```

## Why the workflow proceeds

- The fund exists in the controlled synthetic evidence store.
- The synthetic package is approved for internal use.
- Market exposure, allocation, risks, and approved source IDs are present.
- The request does not contain prohibited investment-recommendation language.
- The output includes required sections and the required disclaimer.

## Control boundary

The draft remains internal and is never published, sent to a client, or treated
as investment advice. Its final state is always:

```text
PENDING_HUMAN_REVIEW
```