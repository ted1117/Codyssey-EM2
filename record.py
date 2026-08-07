from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    total: int
    correct: int

    @property
    def score(self) -> float:
        if self.total == 0:
            return 0.0
        return self.correct / self.total * 100
