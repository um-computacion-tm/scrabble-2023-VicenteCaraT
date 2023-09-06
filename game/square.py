from game.tile import Tile

class Square:
    def __init__(self, row = 0, column = 0, tile = None, multiplier_type = None):
        self.row = row
        self.column = column
        self.multiplier_type = multiplier_type
        self.tile = tile

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

            if square.multiplier_type == 'DL':
                square_score *= 2
            elif square.multiplier_type == 'TL':
                square_score *= 3
            elif square.multiplier_type == 'DW':
                word_multiplier *= 2
            elif square.multiplier_type == 'TW':
                word_multiplier *= 3

            word_score += square_score

        return word_score * word_multiplier




'''    def calculate_score_letter(self):
        if self.tile is None:
            return 0
        self.letter, self.value = self.tile
        score_mult_letter = 1
        if self.multiplier_type in ['DL', 'TL']:
            if self.multiplier_type == 'DL':
                score_mult_letter = 2
            else:
                score_mult_letter = 3
        return self.value * score_mult_letter'''
