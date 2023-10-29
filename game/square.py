from typing import Any
from game.tile import Tile

class Square:
    def __init__(self, multiplier = 1, multiplier_type = 'letter', tile=None, active=True,):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.active = active
        self.tile = tile


    def add_tile(self, tile: Tile):
        self.tile = tile

    def calculate_letter_score(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            result = self.tile.value * self.multiplier
            self.multiplier_type = None
            self.active = False
            return result
        else:
            return self.tile.value

    def __repr__(self): 
        if self.tile:
            return repr(self.tile)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '