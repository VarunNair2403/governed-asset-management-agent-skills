import argparse
from pathlib import Path

from am_skills.harness import AgentHarness
from am_skills.skill_registry import SkillRegistry


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = PROJECT_ROOT / "skills"
DATA_PATH = PROJECT_ROOT / "data" / "synthetic_funds.json"


def list_skills() -> None:
    registry = SkillRegistry(SKILLS_ROOT)
    skills = registry.discover()

    print("Available skills:")

    for skill in skills:
        print(f"\n- {skill.name}")
        print(f"  {skill.description}")


def run_request(request: str) -> None:
    result = AgentHarness(DATA_PATH).run(request)

    print(f"Selected skill: {result.selected_skill or 'none'}")
    print(f"Fund: {result.fund_name or 'none'}")
    print(f"Workflow state: {result.workflow_state}")
    print(f"Message: {result.message}")

    if result.findings:
        print("\nFindings:")
        for finding in result.findings:
            print(f"- [{finding.severity}] {finding.code}: {finding.message}")

    if result.output:
        print("\nDraft:\n")
        print(result.output)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Governed Asset Management Agent Skills prototype"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser(
        "list-skills",
        help="List skill metadata discovered from local SKILL.md files.",
    )

    run_parser = subparsers.add_parser(
        "run",
        help="Run a supported request through the governed agent harness.",
    )
    run_parser.add_argument(
        "--request",
        required=True,
        help="A request for evidence validation or internal research drafting.",
    )

    args = parser.parse_args()

    if args.command == "list-skills":
        list_skills()
    elif args.command == "run":
        run_request(args.request)


if __name__ == "__main__":
    main()