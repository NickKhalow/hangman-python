class Word:
    def guess(self, char: str) -> bool:
        if hasattr(self, '_origin') is not None and hasattr(self._origin, 'guess') is not None:
            return self._origin.guess(char)
        pass

    def done(self) -> bool:
        if hasattr(self, '_origin') is not None and hasattr(self._origin, 'done') is not None:
            return self._origin.done()
        pass

    def describe(self) -> str:
        if hasattr(self, '_origin') is not None and hasattr(self._origin, 'describe') is not None:
            return self._origin.describe()
        pass
