from am_skills.evidence_store import EvidenceStore
from am_skills.models import ValidationFinding, WorkflowResult
from am_skills.validators import REQUIRED_DISCLAIMER, validate_research_draft
from am_skills.workflows.evidence_quality import run_evidence_quality_check


def run_fund_research_draft(
    fund_name: str,
    evidence_store: EvidenceStore,
) -> WorkflowResult:
    """Create a controlled internal research draft from sufficient evidence only."""

    evidence_result = run_evidence_quality_check(fund_name, evidence_store)

    if evidence_result.decision == "FUND_NOT_FOUND":
        return WorkflowResult(
            selected_skill="fund-research-draft",
            fund_name=fund_name,
            workflow_state="FUND_NOT_FOUND",
            message=f"No synthetic evidence package exists for '{fund_name}'.",
            output=None,
            findings=evidence_result.findings,
        )

    if evidence_result.decision != "SUFFICIENT":
        return WorkflowResult(
            selected_skill="fund-research-draft",
            fund_name=fund_name,
            workflow_state="EVIDENCE_INSUFFICIENT",
            message="Research draft was not created because evidence is insufficient.",
            output=None,
            findings=evidence_result.findings,
        )

    fund = evidence_store.get_fund(fund_name)
    assert fund is not None

    source_lines = "\n".join(
        f"- {source['source_id']}: {source['title']}"
        for source in fund["sources"]
    )

    draft = f"""# Internal Research Draft: {fund["fund_name"]}

## Market Exposure

{fund["market_exposure"]}

## Allocation

{fund["allocation"]}

## Key Risks

{fund["risks"]}

## Sources

{source_lines}

## Disclaimer

{REQUIRED_DISCLAIMER}

workflow_state: PENDING_HUMAN_REVIEW
"""

    findings = validate_research_draft(draft)
    has_errors = any(finding.severity == "ERROR" for finding in findings)

    if has_errors:
        return WorkflowResult(
            selected_skill="fund-research-draft",
            fund_name=fund_name,
            workflow_state="VALIDATION_FAILED",
            message="Research draft failed deterministic validation.",
            output=None,
            findings=findings,
        )

    return WorkflowResult(
        selected_skill="fund-research-draft",
        fund_name=fund_name,
        workflow_state="PENDING_HUMAN_REVIEW",
        message="Internal research draft created and routed to human review.",
        output=draft,
        findings=[],
    )