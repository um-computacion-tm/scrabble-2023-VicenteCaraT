from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board
from game.dictionary import(
    DictionaryConnectionError,
    is_in_dictionary
)

class InvalidWordException(Exception):
    pass
class InvalidPlaceWordException(Exception):
    pass
class InvalidWordNoLetters(Exception):
    pass

class ScrabbleGame():
    def __init__(self, total_players: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(total_players):
            self.players.append(Player(id=index))
        self.current_player = None
        self.status = None

    def game_status(self):
        self.status = 'Playing...'
    
    def fist_round_set(self):
        for player in self.players:
            player.refill(7)
        self.next_turn()
    
    def game_over(self):
        self.status = 'Game Over'
        if len(self.bag_tiles.total_tiles) == 0:
            return True
        else:
            return False

    def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')

        return player_count
    
    def word_is_correct(self, word,location,orientation):
        pass

    def fist_round_fist_word(self,word,location, orientation):
        pass
        
    def next_turn(self): 
        if self.current_player == None:
            self.current_player = self.players[0]
        else:            
            index = self.players.index(self.current_player) + 1
            if index >= len(self.players):
                self.current_player = self.players[0]
            else:
                self.current_player = self.players[index]

    def validate_word(self, word, location, orientation): #FIXING
        if not Player().has_letters(word):
            raise InvalidWordNoLetters("No cuenta con las fichas para armar esta palabra")
        if not is_in_dictionary(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.valid_word_in_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
                
    def play(self,word,location,orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_word(word,location,orientation)
        total = self.board.calculate_word_score(words)
        self.players[self.current_player].score += total
        self.next_turn()
        
        
    def get_board():
        '''
        muestra el tablero
        '''
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''

