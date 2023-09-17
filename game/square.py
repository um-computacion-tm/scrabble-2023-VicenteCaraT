from typing import Any
from game.tile import Tile

class Square:
    def __init__(self, tile = None, multiplier_type = None, active = True):
        self.multiplier_type = multiplier_type
        self.tile = tile
        self.active = active

    def add_tile(self, letter:Tile):
        self.tile = letter

    def calculate_letter_score(self):
        letter_multipliers = {'DL': 2, 'TL': 3}
        if self.multiplier_type in letter_multipliers and self.active:
            return self.tile[1] * letter_multipliers[self.multiplier_type]
        else:
            return self.tile[1]

    def calculate_word_score(self):
        word_multipliers = {'DW': 2, 'TW': 3}
        if self.multiplier_type in word_multipliers and self.active:
            return word_multipliers[self.multiplier_type]
        else:
            return 1


    def calculate_score_l_w(self, word):
        word_score = 0
        word_multiplier = 1

        for square in word:
            if square.tile is None:
                return 0

            letter_score = square.calculate_letter_score()
            word_multiplier *= square.calculate_word_score()
            word_score += letter_score

        return word_score * word_multiplier