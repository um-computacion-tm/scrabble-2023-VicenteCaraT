import unittest
from game.board import Board
from game.square import Square
from game.tile import Tile

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
        word_is_valid = board.valid_word_in_board(word, location, orientation)
        assert word_is_valid == True
    

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        word_is_valid = board.valid_word_in_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_word_v_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 3)
        orientation = "V"
        word_is_valid = board.valid_word_in_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_v_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 14)
        orientation = "V"
        word_is_valid = board.valid_word_in_board(word, location, orientation)
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
