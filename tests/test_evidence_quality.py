from pathlib import Path

from am_skills.evidence_store import EvidenceStore
from am_skills.workflows.evidence_quality import run_evidence_quality_check


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "synthetic_funds.json"


def test_complete_fund_evidence_is_sufficient() -> None:
    result = run_evidence_quality_check(
        "Northstar Global Equity Fund",
        EvidenceStore(DATA_PATH),
    )

    assert result.decision == "SUFFICIENT"
    assert result.findings == []


def test_incomplete_fund_evidence_is_insufficient() -> None:
    result = run_evidence_quality_check(
        "Summit Private Credit Fund",
        EvidenceStore(DATA_PATH),
    )

    assert result.decision == "INSUFFICIENT"

    finding_codes = {finding.code for finding in result.findings}

    assert "MISSING_RISKS" in finding_codes
    assert "MISSING_SOURCE_ID" in finding_codes
    assert "STALE_EVIDENCE" in finding_codes


def test_unknown_fund_returns_fund_not_found() -> None:
    result = run_evidence_quality_check(
        "Unknown Alpha Fund",
        EvidenceStore(DATA_PATH),
    )

    assert result.decision == "FUND_NOT_FOUND"
    assert result.findings[0].code == "FUND_NOT_FOUND"