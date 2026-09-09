import argparse
from pathlib import Path

from am_skills.skill_registry import SkillRegistry


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = PROJECT_ROOT / "skills"


def list_skills() -> None:
    registry = SkillRegistry(SKILLS_ROOT)
    skills = registry.discover()

    print("Available skills:")

    for skill in skills:
        print(f"\n- {skill.name}")
        print(f"  {skill.description}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Governed Asset Management Agent Skills prototype"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser(
        "list-skills",
        help="List skill metadata discovered from local SKILL.md files.",
    )

    args = parser.parse_args()

    if args.command == "list-skills":
        list_skills()


if __name__ == "__main__":
    main()