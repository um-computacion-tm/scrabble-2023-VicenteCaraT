from game.bagtiles import BagTiles
from game.tile import Tile

class Player:
    def __init__(self, id = None , bag_tiles = BagTiles() ):
        self.id = id
        self.playertiles = bag_tiles.take(7)
        self.score = 0

    def reset (self):
        self.playertiles = []

    def has_letter(self, word): 
        tiles = [tile.letter for tile in self.playertiles]
        for letter in word:
            if letter in tiles:
                tiles.remove(letter)
            else:
                return False
        return True

    def play_tiles(self, word):
        if self.has_letter(word) is True:
            for letter in word:
                for tile in self.playertiles:
                    if tile.letter == letter:
                        self.playertiles.remove(tile)
                        break
            return self.playertiles
        else:
            return None