from am_skills.evidence_store import EvidenceStore
from am_skills.models import EvidenceQualityResult, ValidationFinding
from am_skills.validators import validate_evidence


def run_evidence_quality_check(
    fund_name: str,
    evidence_store: EvidenceStore,
) -> EvidenceQualityResult:
    """Check whether a synthetic fund evidence package supports internal drafting."""

    fund = evidence_store.get_fund(fund_name)

    if fund is None:
        return EvidenceQualityResult(
            fund_name=fund_name,
            decision="FUND_NOT_FOUND",
            findings=[
                ValidationFinding(
                    severity="ERROR",
                    code="FUND_NOT_FOUND",
                    message=f"No synthetic evidence package exists for '{fund_name}'.",
                )
            ],
        )

    findings = validate_evidence(fund)
    has_errors = any(finding.severity == "ERROR" for finding in findings)

    return EvidenceQualityResult(
        fund_name=fund_name,
        decision="INSUFFICIENT" if has_errors else "SUFFICIENT",
        findings=findings,
    )