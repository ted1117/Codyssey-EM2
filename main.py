from quiz_game import QuizGame
from state_repository import StateRepository


def main() -> None:
    repository = StateRepository()
    game = QuizGame(repository)
    game.run()


if __name__ == "__main__":
    main()
