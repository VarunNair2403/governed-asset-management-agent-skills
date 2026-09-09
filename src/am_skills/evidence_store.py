import json
from pathlib import Path
from typing import Any


class EvidenceStore:
    """Loads approved synthetic fund evidence from a local JSON file."""

    def __init__(self, data_path: Path) -> None:
        self.data_path = data_path

    def get_fund(self, fund_name: str) -> dict[str, Any] | None:
        data = json.loads(self.data_path.read_text(encoding="utf-8"))

        for fund in data["funds"]:
            if fund["fund_name"].casefold() == fund_name.casefold():
                return fund

        return None