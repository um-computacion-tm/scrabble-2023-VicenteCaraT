import unittest
from game.bagtiles import BagTiles
from game.board import Board
from game.player import Player
from game.square import Square
from game.tile import Tile
from game.scrabbleGame import ScrabbleGame
from unittest.mock import patch


class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.total_tiles),
            98,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.total_tiles,
        )

    def test_calculate_total(self):
        bag = BagTiles()
        tiles_created = bag.calculate_tiles()
        self.assertEqual(
            len(tiles_created),
            98,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.total_tiles),
            96,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [('Z', 10),('U', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.total_tiles),
            100,
        )

class TestSquare(unittest.TestCase):
    
    def test_adding_tile(self):
        square = Square(multiplier_type='')
        letter = Tile(letter='X', value='10')
        square.add_tile(letter=letter)
        self.assertEqual(square.tile, letter)
    
    def test_square_with_tile(self):
        square = Square(multiplier_type='DL', tile=('A', 1))
        score = square.calculate_score_l_w([square])
        self.assertEqual(score, 2)

    def test_square_with_no_tile(self):
        square = Square(multiplier_type='DL', tile=None)
        score = square.calculate_score_l_w([square])
        self.assertEqual(score, 0) 

    def test_multuplierLx2(self):
        square = Square(multiplier_type='DL')
        square.tile = ('Z', 10)
        score = square.calculate_score_l_w([square])
        self.assertEqual(
            score,
            20,
        )
    def test_multiplierLx3(self):
        square = Square(multiplier_type='TL')
        square.tile = ('T', 5)
        score = square.calculate_score_l_w([square])
        self.assertEqual(
            score,
            15,
        )

class TestBoard(unittest.TestCase):
    def test_init_(self):
        board = Board ()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
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

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(
            len(player.playertiles),
            0,
        )
    def test_starting_tiles(self):
        player = Player()
        tiles = player.starting_tiles()
        self.assertEqual(
            len(tiles),
            7,
        )

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(total_players= 4)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            4,
        )
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
        controller = Square()
        word = [
            Square(tile=('C', 3)),
            Square(tile=('A', 1)),
            Square(tile=('S', 1)),
            Square(tile=('A', 1)),
        ]
        value = controller.calculate_score_l_w(word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        controller = Square()
        word = [
            Square(multiplier_type='DL', tile=('C', 3)),
            Square(tile=('A', 1)),
            Square(tile=('S', 1)),
            Square(tile=('A', 1)),
        ]
        value = controller.calculate_score_l_w(word)
        self.assertEqual(value, 9)

    def test_with_word_multiplier(self):
        controller = Square()
        word = [
            Square(multiplier_type='DW', tile=('C', 3)),
            Square(tile=('A', 1)),
            Square(tile=('S', 1)),
            Square(tile=('A', 1)),
        ]

        value = controller.calculate_score_l_w(word)
        self.assertEqual(value, 12)

    def test_with_letter_word_multiplier(self):
        controller = Square()
        word = [
            Square(multiplier_type='TW', tile=('C', 3)),
            Square(multiplier_type= 'TL', tile=('A', 1)),
            Square(tile=('S', 1)),
            Square( tile=('A', 1)),
        ]
        value = controller.calculate_score_l_w(word)
        self.assertEqual(value, 24)

    def test_with_letter_word_multiplier_no_active(self):
        controller = Square()
        word = [
            Square(multiplier_type='DW', tile=('C', 3), active=False),
            Square(multiplier_type= 'TL', tile=('A', 1), active=True),
            Square(tile=('S', 1)),
            Square(tile=('A', 1)),
        ]
        value = controller.calculate_score_l_w(word)
        self.assertEqual(value, 8)




if __name__ == '__main__':
    unittest.main()