from game import Game
from word import Word
from typing import Callable
from exceptions import MistakeOutException


class GmSimple(Game):
    def __init__(self, word: Word, user_input: Callable[[], str], user_output: Callable[[str], None]):
        self._word = word
        self._input = user_input
        self._output = user_output

    def play(self):
        try:
            while not self._word.done():
                self._output("Guess a letter: ")
                if self._word.guess(self._input()):
                    self._output("Hit!\n")
                self._output(f"The word: {self._word.describe()}\n\n")
            self._output("You won!")
        except MistakeOutException:
            self._output("You lost.")
