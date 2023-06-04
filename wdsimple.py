import array
from word import Word


class WdSimple(Word):
    def __init__(self, origin: str):
        self._origin = origin
        self._guessed = array.array("b", [False] * len(origin))

    def done(self) -> bool:
        return all(element for element in self._guessed)

    def guess(self, char: str) -> bool:
        hit = False
        for i in range(len(self._origin)):
            if self._origin[i] == char[0] and not self._guessed[i]:
                self._guessed[i] = True
                hit = True
        return hit

    def describe(self) -> str:
        parts = []
        for i in range(len(self._origin)):
            parts.append(self._origin[i] if self._guessed[i] else '?')
        return ''.join(parts)
