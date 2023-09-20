from game.bagtiles import BagTiles

class Player:
    def __init__(self, id = None,  bag = None):
        self.id = id
        self.playertiles = []
        self.score = 0
        self.bag = BagTiles()

    def starting_tiles(self):
        tiles = self.bag.take(7)
        self.playertiles.extend(tiles)
        return self.playertiles  
