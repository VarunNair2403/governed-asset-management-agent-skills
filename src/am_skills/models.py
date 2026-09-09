from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SkillMetadata:
    """Lightweight skill metadata available during progressive discovery."""

    name: str
    description: str
    version: str
    path: Path