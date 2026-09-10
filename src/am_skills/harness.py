from pathlib import Path

from am_skills.evidence_store import EvidenceStore
from am_skills.models import ValidationFinding, WorkflowResult
from am_skills.router import detect_prohibited_language, select_skill
from am_skills.workflows.evidence_quality import run_evidence_quality_check
from am_skills.workflows.fund_research_draft import run_fund_research_draft


SUPPORTED_FUND_NAMES = (
    "Northstar Global Equity Fund",
    "Summit Private Credit Fund",
)


class AgentHarness:
    """Routes supported requests through bounded, deterministic workflows."""

    def __init__(self, data_path: Path) -> None:
        self.evidence_store = EvidenceStore(data_path)

    def run(self, request: str) -> WorkflowResult:
        prohibited_findings = detect_prohibited_language(request)

        if prohibited_findings:
            return WorkflowResult(
                selected_skill=None,
                fund_name=None,
                workflow_state="POLICY_BLOCKED",
                message="Request was blocked by the investment-recommendation policy.",
                output=None,
                findings=prohibited_findings,
            )

        selected_skill = select_skill(request)

        if selected_skill is None:
            return WorkflowResult(
                selected_skill=None,
                fund_name=None,
                workflow_state="UNSUPPORTED_REQUEST",
                message=(
                    "The request does not match a supported skill. Supported skills "
                    "are evidence-quality-check and fund-research-draft."
                ),
                output=None,
                findings=[],
            )

        fund_name = self._extract_fund_name(request)

        if fund_name is None:
            return WorkflowResult(
                selected_skill=selected_skill,
                fund_name=None,
                workflow_state="FUND_NOT_FOUND",
                message="No supported synthetic fund name was found in the request.",
                output=None,
                findings=[
                    ValidationFinding(
                        severity="ERROR",
                        code="FUND_NOT_FOUND",
                        message="No supported synthetic fund name was found in the request.",
                    )
                ],
            )

        if selected_skill == "evidence-quality-check":
            result = run_evidence_quality_check(fund_name, self.evidence_store)

            return WorkflowResult(
                selected_skill=selected_skill,
                fund_name=fund_name,
                workflow_state=result.decision,
                message=f"Evidence quality decision: {result.decision}.",
                output=None,
                findings=result.findings,
            )

        return run_fund_research_draft(fund_name, self.evidence_store)

    @staticmethod
    def _extract_fund_name(request: str) -> str | None:
        normalized_request = request.casefold()

        for fund_name in SUPPORTED_FUND_NAMES:
            if fund_name.casefold() in normalized_request:
                return fund_name

        return None