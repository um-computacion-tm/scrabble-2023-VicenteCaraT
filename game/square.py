from typing import Any
from game.tile import Tile

class Square:
    def __init__(self, multiplier = 1, multiplier_type = '', tile=None, active=True,):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.active = active
        self.tile = tile


    def add_tile(self, letter: Tile):
        self.tile = letter

    def calculate_letter_score(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.tile.value * self.multiplier
        else:
            return self.tile.value


    def __repr__(self): 
        if self.tile:
            return repr(self.tile)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '