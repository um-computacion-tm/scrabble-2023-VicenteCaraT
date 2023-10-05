from game.bagtiles import BagTiles

class Player:
    def __init__(self, id = None, bag = BagTiles()):
        self.id = id
        self.playertiles = []
        self.score = 0
        self.bag = bag

    def fill_tiles (self, count):
        tiles = self.bag.take(count)
        self.playertiles.extend(tiles)
        return self.playertiles

    def reset (self):
        self.playertiles = []

    def has_letters(self, word):
        tiles = [tile[0] for tile in self.playertiles]
        for letter in word:
            if letter not in tiles:
                return False
            else:
                return True

    def show_tiles(self):
        ...
        '''muestra el atril del jugador'''