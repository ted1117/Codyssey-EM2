from quiz import Quiz
from record import Record
from state_repository import StateRepository


class QuizGame:
    def __init__(self, repository: StateRepository):
        self._repository = repository
        self._quizzes, self._best_record = self._repository.load()

    def run(self):
        """게임을 실행하는 메인 루프"""
        actions = {
            1: self.play_quiz,
            2: self.add_quiz,
            3: self.list_quizzes,
            4: self.show_best_score,
            5: self.exit_game,
        }

        while True:
            self.show_menu()
            choice = self.get_number_input("메뉴를 선택하세요: ", 1, 5)
            action = actions.get(choice)
            if action:
                action()
            else:
                print("잘못된 선택입니다. 다시 시도해주세요.")

    @staticmethod
    def show_menu():
        """게임 메뉴를 출력한다."""
        menu: str = """
                    ========================================
                    🎯 나만의 퀴즈 게임 🎯
                    ========================================
                    1. 퀴즈 풀기
                    2. 퀴즈 추가
                    3. 퀴즈 목록
                    4. 점수 확인
                    5. 종료
                    ========================================
                    """
        print(menu)

    def play_quiz(self):
        """퀴즈를 진행한다."""
        # 퀴즈가 없으면 안내 메시지를 출력하고 종료
        if not self._quizzes:
            print("퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        total_questions = len(self._quizzes)
        correct_answers = 0

        for index, quiz in enumerate(self._quizzes, start=1):
            print("-" * 40)
            print(f"[문제 {index}]")
            print(quiz.question)
            print()
            for number, choice in enumerate(quiz.choices, start=1):
                print(f"{number}. {choice}")

            print()

            user_answer = self.get_number_input("정답 입력: ", 1, len(quiz.choices))

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_answers += 1
            else:
                print(
                    f"틀렸습니다. 정답은 {quiz.answer}번: '{quiz.choices[quiz.answer - 1]}'입니다."
                )

        current_record = Record(total=total_questions, correct=correct_answers)
        print("=" * 40)
        print(
            f"결과: {current_record.total}문제 중 "
            f"{current_record.correct}문제 정답! "
            f"({current_record.score:.2f}점)"
        )

        if self.update_best_record(current_record):

            print("새로운 최고 점수입니다!")

        print("=" * 40)

    def add_quiz(self) -> None:
        """새로운 퀴즈를 추가한다."""
        print("\n새로운 퀴즈를 추가합니다.\n")

        question = self.get_text_input("문제를 입력하세요: ")

        choices = [self.get_text_input(f"선택지 {i}: ") for i in range(1, 5)]

        answer = self.get_number_input(
            "정답 번호 (1-4): ",
            1,
            4,
        )

        quiz = Quiz(
            question=question,
            choices=choices,
            answer=answer,
        )

        self._quizzes.append(quiz)

        if self._repository.save(self._quizzes, self._best_record):
            print("\n퀴즈가 추가되었습니다!")
        else:
            self._quizzes.pop()
            print("\n퀴즈 저장에 실패했습니다.")

    def list_quizzes(self):
        pass

    def show_best_score(self):
        """최고 기록과 점수를 출력한다."""
        if self._best_record:
            print(
                f"최고 점수: {self._best_record.score:.2f}점 ({self._best_record.total}문제 중 {self._best_record.correct}문제 정답)"
            )
            return
        print("아직 최고 점수가 없습니다. 퀴즈를 풀어보세요!")
        return

    def update_best_record(self, current_record: Record) -> bool:
        """
        최고 기록을 경신한다.

        Args:
            current_record (Record): 현재 기록

        Returns:
            bool: 최고 기록을 경신했는지 여부
        """
        if self._best_record is None or current_record.score > self._best_record.score:
            self._best_record = current_record
            self._repository.save(self._quizzes, self._best_record)
            return True
        return False

    def get_number_input(self, prompt: str, min_value: int, max_value: int) -> int:
        while True:
            number = input(prompt).strip()
            if not number:
                print("입력이 비어 있습니다. 다시 입력해주세요.")
                continue

            try:
                number = int(number)
            except ValueError:
                print(
                    f"잘못된 입력입니다. {min_value}~{max_value} 사이의 숫자를 입력하세요."
                )
                continue

            if number not in range(min_value, max_value + 1):
                print(
                    f"잘못된 입력입니다. {min_value}~{max_value} 사이의 숫자를 입력하세요."
                )
                continue

            return number

    def get_text_input(self, prompt: str) -> str:
        pass

    def exit_game(self):
        pass
