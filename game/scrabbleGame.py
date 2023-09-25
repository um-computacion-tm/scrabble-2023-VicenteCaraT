from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board

class ScrabbleGame():
    def __init__(self, total_players: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(total_players):
            self.players.append(Player(id=index, bag=self.bag_tiles))
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
    
    def validate_word(self, player, word, location, orientation):
        player_tiles = player.playertiles
        tiles = [tile[0] for tile in player_tiles]
        print(tiles)
        for letter in word:
            if letter not in tiles:
                return False
        if not self.board.word_is_valid(word, location, orientation):
            return False
        
        return True
                
"""    
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
    
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''
"""
