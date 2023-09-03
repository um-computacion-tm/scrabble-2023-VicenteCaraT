from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board

class ScrabbleGame():
    def __init__(self, total_players):
        self.board = Board ()
        self.bag_tiles = BagTiles
        self.players = []
        for _ in range (total_players):
            self.players.append(Player())