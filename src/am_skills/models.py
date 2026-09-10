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
    """A deterministic validation finding."""

    severity: str
    code: str
    message: str


@dataclass(frozen=True)
class EvidenceQualityResult:
    """Structured result returned by the evidence-quality workflow."""

    fund_name: str
    decision: str
    findings: list[ValidationFinding]


@dataclass(frozen=True)
class WorkflowResult:
    """Structured result returned by the governed agent harness."""

    selected_skill: str | None
    fund_name: str | None
    workflow_state: str
    message: str
    output: str | None
    findings: list[ValidationFinding]