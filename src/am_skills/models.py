from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SkillMetadata:
    """Lightweight skill metadata available during progressive discovery."""

    name: str
    description: str
    version: str
    path: Path


@dataclass(frozen=True)
class ValidationFinding:
    """A deterministic evidence-validation finding."""

    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class EvidenceQualityResult:
    """Structured result returned by the evidence-quality workflow."""

    fund_name: str
    decision: str
    findings: list[ValidationFinding]