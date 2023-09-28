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
