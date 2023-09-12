from game.tile import Tile

class Square:
    def __init__(self, tile = None, multiplier_type = None, active = True):
        self.multiplier_type = multiplier_type
        self.tile = tile
        self.active = active

    def add_tile(self, letter:Tile):
        self.tile = letter

    def calculate_score_l_w(self, word):
        word_score = 0
        word_multiplier = 1
        letter_multipliers = {'DL': 2, 'TL': 3}
        word_multipliers = {'DW': 2, 'TW': 3}

        for square in word:
            if square.tile is None:
                return 0

            value = square.tile[1]
            square_score = value

            if square.multiplier_type in letter_multipliers and square.active:
                square_score *= letter_multipliers[square.multiplier_type]

            if square.multiplier_type in word_multipliers and square.active:
                word_multiplier *= word_multipliers[square.multiplier_type]

            word_score += square_score

        return word_score * word_multiplier