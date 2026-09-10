import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_evaluation_suite_passes() -> None:
    result = subprocess.run(
        [sys.executable, "evals/run_evals.py"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Evaluation summary: 5/5 passed" in result.stdout