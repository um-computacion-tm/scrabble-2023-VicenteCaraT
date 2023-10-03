import unittest
from game.bagtiles import BagTiles
from game.board import Board
from game.player import Player
from game.square import Square
from game.tile import Tile
from game.scrabbleGame import ScrabbleGame
from unittest.mock import patch
from game.dictionary import(
    DictionaryConnectionError,
    is_in_dictionary
)


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


class TestBagTiles(unittest.TestCase):

    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.total_tiles),98)
        self.assertEqual(patch_shuffle.call_count,1)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.total_tiles,)

    def test_calculate_total(self):
        bag = BagTiles()
        tiles_created = bag.calculate_tiles()
        self.assertEqual(len(tiles_created),98)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(bag.total_tiles), 96)
        self.assertEqual(len(tiles),2)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [('Z', 10),('U', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.total_tiles),100)

class TestSquare(unittest.TestCase):
    
    def test_adding_tile(self):
        square = Square(multiplier_type='')
        letter = Tile(letter='X', value='10')
        square.add_tile(letter=letter)
        self.assertEqual(square.tile, letter)
    
    def test_square_with_tile(self):
        square = Square(multiplier=2, multiplier_type='letter')
        square.tile = Tile(letter='A', value=1)
        score = square.calculate_letter_score()
        self.assertEqual(score, 2)

    def test_square_with_no_tile(self):
        square = Square( multiplier_type='DL')
        score = square.calculate_letter_score()
        self.assertEqual(score, 0) 

    def test_multuplierLx2(self):
        square = Square(multiplier=2, multiplier_type='letter')
        square.tile = Tile(letter='Z', value=10)
        score = square.calculate_letter_score()
        self.assertEqual(score,20)

    def test_multiplierLx3(self):
        square = Square(multiplier=3 ,multiplier_type='letter')
        square.tile = Tile(letter='T', value=5)
        score = square.calculate_letter_score()
        self.assertEqual(score,15)

class TestBoard(unittest.TestCase):
    
    def test_init_(self):
        board = Board ()
        self.assertEqual(len(board.grid),15)
        self.assertEqual(len(board.grid[0]),15)

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.word_is_valid(word, location, orientation)
        assert word_is_valid == True
    

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.word_is_valid(word, location, orientation)
        assert word_is_valid == False
    
    def test_word_v_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 3)
        orientation = "V"
        word_is_valid = board.word_is_valid(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_v_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 14)
        orientation = "V"
        word_is_valid = board.word_is_valid(word, location, orientation)
        assert word_is_valid == False
    
    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty() == True
    
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][2].add_tile(letter=Tile(letter='C', value=1))
        assert board.is_empty() == False

'''
    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_tile(letter=Tile('C', 1))
        board.grid[8][7].add_tile(letter=Tile('A', 1))
        board.grid[9][7].add_tile(letter=Tile('S', 1))
        board.grid[10][7].add_tile(letter=Tile('A', 1))
        word = 'Facultad'
        location = (8,6)
        orientation = 'H'
        word_valid = board.word_is_valid(word, location, orientation)
        assert word_valid == True
'''
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(len(player.playertiles),0)
    
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

class TestCalculateWordValue(unittest.TestCase):
    
    def test_calculate_word(self):
        board = Board()
        word = [
            Square(tile=Tile('C', 3)),
            Square(tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_score(word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        board = Board()
        word = [
            Square(multiplier=2, multiplier_type='letter', tile=Tile('C', 3)),
            Square(tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_score(word)
        self.assertEqual(value, 9)

    def test_with_word_multiplier(self):
        board = Board()
        word = [
            Square(multiplier=2, multiplier_type='word', tile=Tile('C', 3)),
            Square(tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]

        value = board.calculate_word_score(word)
        self.assertEqual(value, 12)

    def test_with_letter_word_multiplier(self):
        board = Board()
        word = [
            Square(multiplier=3, multiplier_type='letter', tile=Tile('C', 3)),
            Square(multiplier=2, multiplier_type= 'word', tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_score(word)
        self.assertEqual(value, 24)

    def test_with_letter_word_multiplier_no_active(self):
        board = Board()
        word = [
            Square(multiplier=2, multiplier_type='word', tile=Tile('C', 3), active=False),
            Square(multiplier=3, multiplier_type= 'letter', tile=Tile('A', 1), active=True),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_score(word)
        self.assertEqual(value, 8)

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

class TestDiccionary(unittest.TestCase):
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )
    def test_valid(self, search_by_word_patched):
        self.assertTrue(is_in_dictionary('hola'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )
    def test_invalid(self, search_by_word_patched):
        self.assertFalse(is_in_dictionary('asd'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )
    def test_connection_error(self, search_by_word_patched):
        with self.assertRaises(DictionaryConnectionError):
            is_in_dictionary('hola')


if __name__ == '__main__':
    unittest.main()