from datetime import date

from am_skills.models import ValidationFinding
from am_skills.router import PROHIBITED_TERMS


REQUIRED_EVIDENCE_FIELDS = (
    "market_exposure",
    "allocation",
    "risks",
    "sources",
)

REQUIRED_DRAFT_SECTIONS = (
    "## Market Exposure",
    "## Allocation",
    "## Key Risks",
    "## Sources",
    "## Disclaimer",
)

REQUIRED_DISCLAIMER = (
    "Synthetic demonstration data only. This internal research-preparation draft "
    "is not investment advice, a recommendation, or a solicitation. It must be "
    "reviewed by an authorized human reviewer before any further use."
)

MAX_EVIDENCE_AGE_DAYS = 365


def validate_evidence(fund: dict) -> list[ValidationFinding]:
    """Return deterministic findings for a synthetic fund evidence package."""

    findings: list[ValidationFinding] = []

    if fund.get("approval_status") != "APPROVED_INTERNAL_SYNTHETIC":
        findings.append(
            ValidationFinding(
                severity="ERROR",
                code="UNAPPROVED_PACKAGE",
                message="Evidence package is not approved for internal synthetic use.",
            )
        )

    for field in REQUIRED_EVIDENCE_FIELDS:
        if not fund.get(field):
            findings.append(
                ValidationFinding(
                    severity="ERROR",
                    code=f"MISSING_{field.upper()}",
                    message=f"Required evidence field is missing or empty: {field}.",
                )
            )

    as_of_date = fund.get("as_of_date")
    if as_of_date:
        evidence_date = date.fromisoformat(as_of_date)
        evidence_age_days = (date.today() - evidence_date).days

        if evidence_age_days > MAX_EVIDENCE_AGE_DAYS:
            findings.append(
                ValidationFinding(
                    severity="WARNING",
                    code="STALE_EVIDENCE",
                    message=(
                        f"Evidence is {evidence_age_days} days old, exceeding the "
                        f"{MAX_EVIDENCE_AGE_DAYS}-day freshness threshold."
                    ),
                )
            )
    else:
        findings.append(
            ValidationFinding(
                severity="ERROR",
                code="MISSING_AS_OF_DATE",
                message="Evidence package is missing an as-of date.",
            )
        )

    for source in fund.get("sources", []):
        if not source.get("source_id"):
            findings.append(
                ValidationFinding(
                    severity="ERROR",
                    code="MISSING_SOURCE_ID",
                    message="A source record is missing a source ID.",
                )
            )

        if not source.get("approved"):
            findings.append(
                ValidationFinding(
                    severity="ERROR",
                    code="UNAPPROVED_SOURCE",
                    message=(
                        f"Source '{source.get('title', 'unknown')}' is not approved."
                    ),
                )
            )

    return findings


def validate_research_draft(draft: str) -> list[ValidationFinding]:
    """Return deterministic findings for a generated internal research draft."""

    findings: list[ValidationFinding] = []

    for section in REQUIRED_DRAFT_SECTIONS:
        if section not in draft:
            findings.append(
                ValidationFinding(
                    severity="ERROR",
                    code="MISSING_REQUIRED_SECTION",
                    message=f"Draft is missing required section: {section}.",
                )
            )

    if REQUIRED_DISCLAIMER not in draft:
        findings.append(
            ValidationFinding(
                severity="ERROR",
                code="MISSING_REQUIRED_DISCLAIMER",
                message="Draft is missing the required disclaimer.",
            )
        )

    normalized_draft = draft.casefold()

    for term in PROHIBITED_TERMS:
        if term in normalized_draft:
            findings.append(
                ValidationFinding(
                    severity="ERROR",
                    code="PROHIBITED_RECOMMENDATION_LANGUAGE",
                    message=f"Prohibited recommendation language detected: '{term}'.",
                )
            )

    return findings