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
        pass

    def add_quiz(self):
        pass

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
                print("유효한 숫자가 아닙니다. 다시 입력해주세요.")
                continue

            if number not in range(min_value, max_value + 1):
                print(
                    f"입력이 범위를 벗어났습니다. {min_value}에서 {max_value} 사이의 숫자를 입력해주세요."
                )
                continue

            return number

    def get_text_input(self, prompt: str) -> str:
        pass

    def exit_game(self):
        pass
