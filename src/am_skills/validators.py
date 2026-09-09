from datetime import date

from am_skills.models import ValidationFinding


REQUIRED_EVIDENCE_FIELDS = (
    "market_exposure",
    "allocation",
    "risks",
    "sources",
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