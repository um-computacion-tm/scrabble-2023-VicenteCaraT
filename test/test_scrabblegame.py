import unittest
from game.scrabbleGame import ScrabbleGame

class TestScrabblePlayers(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(total_players= 4)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),4)
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]  
    
    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]
    
class TestScrableWord(unittest.TestCase):
    
    def test_validate_word_with_valid_word_L_separated(self):
        scrabble_game = ScrabbleGame(total_players=4)
        scrabble_game.players[0].playertiles = [('H', 4), ('O', 1), ('L', 1),('A', 1)]
        player = scrabble_game.players[0]
        word = "HOLA"
        location = (3, 3)
        orientation = "H"
        result = scrabble_game.validate_word(player, word, location, orientation)
        self.assertEqual(result, True)
    

    def test_validate_word_with_invalid_word(self):
        scrabble_game = ScrabbleGame(total_players=4)
        scrabble_game.players[0].playertiles = [('H', 4), ('E', 1), ('L', 1), ('L',1), ('O', 1)]
        player = scrabble_game.players[0]
        word = "INVALID"
        location = (5, 5)
        orientation = "H"
        result = scrabble_game.validate_word(player, word, location, orientation)
        self.assertEqual(result, False)

    def test_validate_word_out_of_board(self):
        scrabble_game = ScrabbleGame(total_players=4)
        scrabble_game.players[0].playertiles = [('B', 3),('I', 1),('Z', 8), ('C', 1), ('O', 1), ('C', 1), ('H',1), ('O',1)]
        player = scrabble_game.players[0]
        word = "bizcocho"
        location = (14, 13)
        orientation = "V"
        result = scrabble_game.validate_word(player, word, location, orientation)
        self.assertEqual(result, False)
    
    def test_validate_word_not_in_dictionary(self):
        scrabble_game = ScrabbleGame(total_players=4)
        scrabble_game.players[0].playertiles = [('A', 1), ('S', 1), ('D', 2)]
        player = scrabble_game.players[0]
        word = 'asd'
        location = (3, 5)
        orientation = 'H'
        result = scrabble_game.validate_word(player, word, location,orientation)
        self.assertEqual(result, False)
        '''
'''    
    def test_validate_word_with_valid_word_RR(self):
        scrabble_game = ScrabbleGame(total_players=4)
        scrabble_game.players[0].playertiles = [('P', 3),('E', 1),('RR', 8),('O', 1)]
        player = scrabble_game.players[0]
        word = "perro"
        location = (3, 2)
        orientation = "H"
        result = scrabble_game.validate_word(player, word, location, orientation)
        self.assertEqual(result, True)
    
    def test_validate_word_with_valid_word_Ch_together(self):
        scrabble_game = ScrabbleGame(total_players=4)
        scrabble_game.players[0].playertiles = [('Ch', 8), ('A', 1), ('Q', 5), ('E', 1), ('T', 1), ('A', 1)]
        player = scrabble_game.players[0]
        word = "chaqueta"
        location = (3, 3)
        orientation = "H"
        result = scrabble_game.validate_word(player, word, location, orientation)
        self.assertEqual(result, True)