import json
from dataclasses import asdict
from pathlib import Path

from quiz import Quiz
from record import Record


class StateRepository:
    """
    state.json 파일의 저장과 불러오기를 담당하는 저장소 클래스
    """

    def __init__(self, file_path: str = "state.json"):
        self._file_path = Path(file_path)

    def load(self) -> tuple[list[Quiz], Record | None]:
        """
        state.json에서 퀴즈 목록과 최고 점수를 불러온다.

        파일이 없거나 손상된 경우 기본 퀴즈와 None을 반환한다.

        Returns:
            tuple[list[Quiz], Record | None]: (퀴즈 목록, 최고 기록)
        """
        if not self._file_path.exists():
            return self._create_default_quizzes(), None
        try:
            with self._file_path.open("r", encoding="utf-8") as f:
                state = json.load(f)

            quizzes = [
                Quiz.from_dict(quiz_dict) for quiz_dict in state.get("quizzes", [])
            ]

            record_data: dict = state.get("best_record")
            best_record: Record | None = Record(**record_data) if record_data else None

            return quizzes, best_record
        except (
            OSError,
            AttributeError,
            json.JSONDecodeError,
            KeyError,
            TypeError,
            ValueError,
        ) as e:
            print(f"저장 파일을 불러올 수 없습니다.: {e}")
            print("기본 데이터로 복구합니다.")

            return self._create_default_quizzes(), None

    def save(self, quizzes: list[Quiz], best_record: Record | None) -> bool:
        """
        퀴즈 목록과 최고 점수를 state.json에 저장한다.

        Args:
            quizzes (list[Quiz]): 저장할 퀴즈 목록
            best_record (Record | None): 저장할 최고 기록

        Returns:
            bool: 저장 성공 여부
        """
        state = {
            "quizzes": [quiz.to_dict() for quiz in quizzes],
            "best_record": asdict(best_record) if best_record else None,
        }

        try:
            with self._file_path.open("w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent=4)

            return True
        except OSError as e:
            print(f"저장 파일을 저장할 수 없습니다.: {e}")
            return False

    def _create_default_quizzes(self) -> list[Quiz]:
        """
        기본 퀴즈 목록을 생성한다.

        Returns:
            list[Quiz]: 기본 퀴즈 목록
        """
        default_quizzes = [
            Quiz(
                question="다음 중 파이썬의 데이터 타입이 아닌 것은?",
                choices=["list", "tuple", "dictionary", "array"],
                answer=4,
            ),
            Quiz(
                question="다음 중 파이썬에서 반복문을 종료하는 키워드는?",
                choices=["break", "continue", "pass", "exit"],
                answer=1,
            ),
            Quiz(
                question="다음 중 파이썬에서 함수를 정의하는 키워드는?",
                choices=["def", "function", "lambda", "define"],
                answer=1,
            ),
            Quiz(
                question="다음 중 파이썬에서 예외 처리를 위해 사용하는 키워드는?",
                choices=["try", "catch", "except", "finally"],
                answer=3,
            ),
            Quiz(
                question="다음 중 파이썬에서 리스트에 요소를 추가하는 메서드는?",
                choices=["append", "add", "insert_item", "push"],
                answer=1,
            ),
        ]
        return default_quizzes
