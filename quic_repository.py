import json
from pathlib import Path
from typing import Any


class QuizRepository:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def _load_data(self) -> dict[str, Any]:
        with self.file_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _save_data(self, data: dict[str, Any]) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_quizzes(self) -> list[dict[str, Any]]:
        return self._load_data()["quizzes"]

    def get_best_score(self) -> int:
        return self._load_data()["best_score"]

    def update_best_score(self, score: int) -> bool:
        data = self._load_data()

        if score <= data["best_score"]:
            return False

        data["best_score"] = score
        self._save_data(data)
        return True

