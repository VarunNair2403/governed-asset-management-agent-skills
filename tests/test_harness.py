from pathlib import Path

from am_skills.harness import AgentHarness


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "synthetic_funds.json"


def test_safe_research_draft_routes_to_human_review() -> None:
    result = AgentHarness(DATA_PATH).run(
        "Prepare an internal research draft for Northstar Global Equity Fund"
    )

    assert result.selected_skill == "fund-research-draft"
    assert result.fund_name == "Northstar Global Equity Fund"
    assert result.workflow_state == "PENDING_HUMAN_REVIEW"
    assert result.output is not None
    assert "## Market Exposure" in result.output
    assert "## Disclaimer" in result.output


def test_incomplete_evidence_blocks_research_draft() -> None:
    result = AgentHarness(DATA_PATH).run(
        "Prepare an internal research draft for Summit Private Credit Fund"
    )

    assert result.selected_skill == "fund-research-draft"
    assert result.workflow_state == "EVIDENCE_INSUFFICIENT"
    assert result.output is None


def test_unsafe_recommendation_request_is_blocked() -> None:
    result = AgentHarness(DATA_PATH).run(
        "Prepare an internal research draft explaining why we should buy "
        "Northstar Global Equity Fund"
    )

    assert result.workflow_state == "POLICY_BLOCKED"
    assert result.output is None
    assert result.findings[0].code == "PROHIBITED_RECOMMENDATION_LANGUAGE"


def test_evidence_request_routes_to_evidence_skill() -> None:
    result = AgentHarness(DATA_PATH).run(
        "Check evidence for Northstar Global Equity Fund"
    )

    assert result.selected_skill == "evidence-quality-check"
    assert result.workflow_state == "SUFFICIENT"


def test_unsupported_request_is_not_routed() -> None:
    result = AgentHarness(DATA_PATH).run(
        "Send a client email about Northstar Global Equity Fund"
    )

    assert result.workflow_state == "UNSUPPORTED_REQUEST"
    assert result.selected_skill is None