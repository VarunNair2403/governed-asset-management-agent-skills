from pathlib import Path

from am_skills.models import SkillMetadata


class SkillRegistry:
    """Discovers Agent Skills from local SKILL.md files."""

    def __init__(self, skills_root: Path) -> None:
        self.skills_root = skills_root

    def discover(self) -> list[SkillMetadata]:
        skills: list[SkillMetadata] = []

        for skill_file in sorted(self.skills_root.glob("*/SKILL.md")):
            metadata = self._parse_metadata(skill_file)
            skills.append(metadata)

        return skills

    @staticmethod
    def _parse_metadata(skill_file: Path) -> SkillMetadata:
        content = skill_file.read_text(encoding="utf-8")

        if not content.startswith("---\n"):
            raise ValueError(f"{skill_file} must start with YAML frontmatter.")

        _, frontmatter, _ = content.split("---", maxsplit=2)
        fields: dict[str, str] = {}

        for line in frontmatter.strip().splitlines():
            key, value = line.split(":", maxsplit=1)
            fields[key.strip()] = value.strip()

        required_fields = {"name", "description", "version"}
        missing_fields = required_fields - fields.keys()

        if missing_fields:
            missing = ", ".join(sorted(missing_fields))
            raise ValueError(f"{skill_file} is missing frontmatter fields: {missing}")

        return SkillMetadata(
            name=fields["name"],
            description=fields["description"],
            version=fields["version"],
            path=skill_file,
        )