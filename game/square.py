from game.tile import Tile

class Square:
    def __init__(self, row = 0, column = 0, tile = None, multiplier_type = None):
        self.row = row
        self.column = column
        self.multiplier_type = multiplier_type
        self.tile = tile

    def add_tile(self, letter:Tile):
        self.tile = letter

    def calculate_score_letter(self):
        if self.tile is None:
            return 0
        self.letter, self.value = self.tile
        score_mult_letter = 1
        if self.multiplier_type in ['DL', 'TL']:
            if self.multiplier_type == 'DL':
                score_mult_letter = 2
            else:
                score_mult_letter = 3
        return self.value * score_mult_letter
    