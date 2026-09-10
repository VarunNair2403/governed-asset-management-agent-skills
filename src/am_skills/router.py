from am_skills.models import ValidationFinding


RESEARCH_KEYWORDS = (
    "research draft",
    "research report",
    "prepare an internal research",
    "draft a research",
    "prepare a research",
)

EVIDENCE_KEYWORDS = (
    "check evidence",
    "validate evidence",
    "assess evidence",
    "evidence quality",
)

PROHIBITED_TERMS = (
    "buy",
    "sell",
    "hold",
    "target price",
    "target-price",
    "overweight",
    "underweight",
    "strong buy",
    "strong sell",
)


def detect_prohibited_language(request: str) -> list[ValidationFinding]:
    """Return findings for explicitly prohibited recommendation language."""

    normalized_request = request.casefold()
    findings: list[ValidationFinding] = []

    for term in PROHIBITED_TERMS:
        if term in normalized_request:
            findings.append(
                ValidationFinding(
                    severity="ERROR",
                    code="PROHIBITED_RECOMMENDATION_LANGUAGE",
                    message=f"Prohibited recommendation language detected: '{term}'.",
                )
            )

    return findings


def select_skill(request: str) -> str | None:
    """Select one supported skill through simple deterministic intent matching."""

    normalized_request = request.casefold()

    if any(keyword in normalized_request for keyword in EVIDENCE_KEYWORDS):
        return "evidence-quality-check"

    if any(keyword in normalized_request for keyword in RESEARCH_KEYWORDS):
        return "fund-research-draft"

    return None