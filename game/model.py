import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            ('A', 1, 12),
            ('E', 1, 12),
            ('I', 1, 6),
            ('L', 1, 4),
            ('N', 1, 5),
            ('O', 1, 9),
            ('R', 1, 5),
            ('S', 1, 6),
            ('T', 1, 4),
            ('U', 1, 5),
            ('D', 2, 5),
            ('G', 2, 2),
            ('B', 3, 2),
            ('C', 3, 4),
            ('M', 3, 2),
            ('P', 3, 2),
            ('F', 4, 1),
            ('H', 4, 2),
            ('V', 4, 1),
            ('Y', 4, 1),
            ('Ch', 5, 1),
            ('Q', 5, 1),
            ('J', 8, 1),
            ('LL', 8, 1),
            ('Ñ', 8, 1),
            ('RR', 8, 1),
            ('X', 1, 1),
            ('Z', 10, 1),
        ]

        self.total_tiles = self.calculate_tiles()
        random.shuffle(self.total_tiles)

    def calculate_tiles(self):
        total_tiles = []
        for letter, value, total in self.tiles:
            total_tiles.extend([(letter,value)] * total)
        return total_tiles
        
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.total_tiles.pop())
        return tiles
    
    def put(self, tiles):
        self.total_tiles.extend(tiles)

class Square(Tile):
    def __init__(self, row, column, multiplier_type = None):
        super().__init__(letter='', value=0)
        self.row = row
        self.column = column
        self.multiplier_type = multiplier_type
        self.tile = None

    def calculate_score(self):
        self.letter, self.value = self.tile
        score_mult = 1
        if self.multiplier_type in ['DL', 'TL']:
            if self.multiplier_type == 'DL':
                score_mult = 2
            else:
                score_mult = 3
        return self.value * score_mult