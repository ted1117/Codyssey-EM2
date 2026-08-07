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
