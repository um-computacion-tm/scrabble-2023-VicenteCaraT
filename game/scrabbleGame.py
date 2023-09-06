from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board

class ScrabbleGame():
    def __init__(self, total_players):
        self.board = Board()
        self.bag_tiles = BagTiles
        self.players = []
        for _ in range (total_players):
            self.players.append(Player())
        self.current_player = None

    def next_turn(self):
        if self.current_player == None:
            self.current_player = self.players[0]
        else:            
            index = self.players.index(self.current_player) + 1
            if index >= len(self.players):
                self.current_player = self.players[0]
            else:
                self.current_player = self.players[index]
