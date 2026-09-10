import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from am_skills.harness import AgentHarness


CASES_PATH = PROJECT_ROOT / "evals" / "cases.json"
DATA_PATH = PROJECT_ROOT / "data" / "synthetic_funds.json"


def main() -> int:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    harness = AgentHarness(DATA_PATH)
    passed = 0

    for case in cases:
        result = harness.run(case["request"])

        matches_skill = result.selected_skill == case["expected_skill"]
        matches_state = result.workflow_state == case["expected_state"]
        passed_case = matches_skill and matches_state

        if passed_case:
            passed += 1
            status = "PASS"
        else:
            status = "FAIL"

        print(f"{status} {case['id']}: {case['description']}")

        if not passed_case:
            print(f"  Expected skill: {case['expected_skill']}")
            print(f"  Actual skill:   {result.selected_skill}")
            print(f"  Expected state: {case['expected_state']}")
            print(f"  Actual state:   {result.workflow_state}")

    total = len(cases)
    print(f"\nEvaluation summary: {passed}/{total} passed")

    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())