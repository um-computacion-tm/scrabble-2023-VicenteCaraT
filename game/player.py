from game.bagtiles import BagTiles
from game.tile import Tile

class Player:
    def __init__(self, id = None , bag_tiles = None):
        self.id = id
        self.playertiles = []
        self.score = 0
        self.bag_tiles = bag_tiles

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
    
    def refill(self, count): #Fixing
        total_tiles = len(self.playertiles)
        if total_tiles < 7:
            draw_tiles = BagTiles().take(count)
            self.playertiles.extend(draw_tiles)
    
    def new_tiles(self, index_to_change, bag_tiles):
        if all(0 <= index < len(self.playertiles) for index in index_to_change):

            new_tiles = bag_tiles.take(len(index_to_change))

            returned_tiles = [self.playertiles[index] for index in index_to_change]
            bag_tiles.put(returned_tiles)

            for index, new_tile in zip(index_to_change, new_tiles):
                self.playertiles[index] = new_tile

            return returned_tiles, new_tiles
        else:
            #levantar una excepción
            return None


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
    
    def show_tiles(self):
        return self.playertiles
    
    def show_score(self):
        return self.score
    
    def __str__(self): #New
        player_info = f"Player ID: {self.id}\n"
        tiles_info = f"Tiles: {' '.join(tile.letter for tile in self.playertiles)}\n"
        score_info = f"Score: {self.score}\n"
        return player_info + tiles_info + score_info

