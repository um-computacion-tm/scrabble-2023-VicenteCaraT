from game.bagtiles import BagTiles
from game.player import Player
from game.board import Board
from game.dictionary import(
    DictionaryConnectionError,
    is_in_dictionary
)

class InvalidWordException(Exception):#NEW
    pass
class InvalidPlaceWordException(Exception):#NEW
    pass
class InvalidWordNoLetters(Exception):
    pass



class ScrabbleGame():
    def __init__(self, total_players: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for index in range(total_players):
            self.players.append(Player(id=index, bag_tiles = self.bag_tiles))
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

    def validate_word(self, word, location, orientation): #FIXING
        if not Player().has_letters(word):
            raise InvalidWordNoLetters("No cuenta con las fichas para armar esta palabra")
        if not is_in_dictionary(word):
            raise InvalidWordException("Su palabra no existe en el diccionario")
        if not self.board.valid_word_in_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")
                
"""    
    def play():
        '''
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word,location,orientation)
        total = calculate_words_value(words)
        self.player[self.currenplayer].score += total
        self.next_turn
        esto es lo que tiene que funcionar en si
        '''
    def get_board():
        '''
        muestra el tablero
        '''
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''
"""
