import random
from game.tile import Tile

class BagTiles:
    def __init__(self):
        self.tiles = [
            ('?', 0, 2),
            ('A', 1, 12),
            ('E', 1, 12),
            ('I', 1, 6),
            ('L', 1, 6),
            ('N', 1, 5),
            ('O', 1, 9),
            ('R', 1, 7),
            ('S', 1, 6),
            ('T', 1, 4),
            ('U', 1, 5),
            ('D', 2, 5),
            ('G', 2, 2),
            ('B', 3, 2),
            ('C', 3, 5),
            ('M', 3, 2),
            ('P', 3, 2),
            ('F', 4, 1),
            ('H', 4, 3),
            ('V', 4, 1),
            ('Y', 4, 1),
            ('Q', 5, 1),
            ('J', 8, 1),
            ('Ñ', 8, 1),
            ('X', 10, 1),
            ('Z', 10, 1),
        ]

        self.total_tiles = self.calculate_tiles()
        random.shuffle(self.total_tiles)

    def calculate_tiles(self):
        total_tiles = []
        for letter, value, total in self.tiles:
            total_tiles.extend([Tile(letter,value)] * total)
        return total_tiles
        
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.total_tiles.pop())
        return tiles
    
    def put(self, tiles):
        self.total_tiles.extend(tiles)