from exceptions import MistakeOutException
from word import Word
from typing import Callable


class WdMistakes(Word):
    def __init__(self, origin: Word, user_output: Callable[[str], None], max_attempts: int = 5):
        self._output = user_output
        self._origin = origin
        self._max = max_attempts
        self._mistakes = 0

    def guess(self, char: str) -> bool:
        success = self._origin.guess(char)
        if not success:
            self._mistakes += 1
            if self._mistakes >= self._max:
                raise MistakeOutException()
            self._output(f"Missed, mistake #{self._mistakes} out of {self._max}\n")
        return success
