# Insufficient Evidence Example

## Request

```text
Prepare an internal research draft for Summit Private Credit Fund
```

## Expected workflow result

```text
Selected skill: fund-research-draft
Fund: Summit Private Credit Fund
Workflow state: EVIDENCE_INSUFFICIENT
Message: Research draft was not created because evidence is insufficient.
```

## Expected deterministic findings

```text
[ERROR] MISSING_RISKS
[WARNING] STALE_EVIDENCE
[ERROR] MISSING_SOURCE_ID
```

## Why the workflow stops

The harness does not infer missing risk information, fabricate a source ID, or
continue to draft around insufficient evidence. It returns the structured
findings and requires the missing information to be resolved before a draft can
be created.