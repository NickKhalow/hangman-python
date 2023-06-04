from abc import ABC, abstractmethod


class Word(ABC):

    @abstractmethod
    def guess(self, char: str) -> bool:
        pass

    @abstractmethod
    def done(self) -> bool:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass
