from game.tile import Tile

class Square:
    def __init__(self, row = 0, column = 0, tile = None, multiplier_type = None, active = True):
        self.row = row
        self.column = column
        self.multiplier_type = multiplier_type
        self.tile = tile
        self.active=active

    def add_tile(self, letter:Tile):
        self.tile = letter

    def calculate_score_l_w(self, word):
        word_score = 0
        word_multiplier = 1

        for square in word:
            if square.tile is None:
                continue

            value = square.tile[1]
            square_score = value

            if square.multiplier_type == 'DL' and square.active:
                    square_score *= 2
            elif square.multiplier_type == 'TL' and square.active:
                    square_score *= 3
            elif square.multiplier_type == 'DW' and square.active:
                    word_multiplier *= 2
            elif square.multiplier_type == 'TW' and square.active:
                    word_multiplier *= 3

            word_score += square_score

        return word_score * word_multiplier