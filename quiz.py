class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        if not self._validate_question(question):
            raise ValueError("문제가 올바르지 않습니다.")
        if not self._validate_choices(choices):
            raise ValueError("선택지가 올바르지 않습니다.")
        if not self._validate_answer(answer, choices):
            raise ValueError("정답이 올바르지 않습니다.")

        self._question = question
        self._choices = choices
        self._answer = answer

    @property
    def question(self) -> str:
        return self._question

    @property
    def choices(self) -> list[str]:
        return self._choices.copy()

    @property
    def answer(self) -> int:
        return self._answer

    @staticmethod
    def _validate_question(question) -> bool:
        return isinstance(question, str) and bool(question.strip())

    @staticmethod
    def _validate_choices(choices) -> bool:
        return (
            isinstance(choices, list)
            and len(choices) == 4
            and all(
                isinstance(choice, str) and bool(choice.strip()) for choice in choices
            )
        )

    @staticmethod
    def _validate_answer(answer, choices) -> bool:
        return isinstance(answer, int) and 1 <= answer <= len(choices)

    def is_correct(self, user_answer: int) -> bool:
        return user_answer == self._answer

    def to_dict(self) -> dict:
        return {
            "question": self._question,
            "choices": self._choices,
            "answer": self._answer,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
        )


def create_default_quizzes() -> list[Quiz]:
    """프로그램에서 사용할 기본 퀴즈 목록을 생성한다."""
    return [
        Quiz(
            question="파이썬에서 화면에 값을 출력할 때 사용하는 함수는?",
            choices=["input()", "print()", "output()", "display()"],
            answer=2,
        ),
        Quiz(
            question="파이썬에서 리스트의 첫 번째 요소에 접근할 때 사용하는 인덱스는?",
            choices=["0", "1", "-1", "first"],
            answer=1,
        ),
        Quiz(
            question="조건에 따라 다른 코드를 실행할 때 사용하는 파이썬 키워드는?",
            choices=["for", "if", "when", "switch"],
            answer=2,
        ),
        Quiz(
            question="파이썬에서 몫을 구하는 연산자는?",
            choices=["/", "%", "//", "**"],
            answer=3,
        ),
        Quiz(
            question="파이썬에서 값이 없음을 나타내는 특수한 값은?",
            choices=["Empty", "Null", "None", "Nothing"],
            answer=3,
        ),
    ]
