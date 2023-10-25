import unittest
from game.board import Board, InvalidLocation
from game.square import Square
from game.tile import Tile
import difflib

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
        board.grid[7][7].add_tile(tile=Tile(letter='C', value=1))
        assert board.is_empty() == False
    
    def test_put_word_horizontal(self):
        board = Board()
        word = 'HOLA'
        location = (7,7)
        orientation = 'H'
        board.put_word(word, location, orientation)

        for i, letter in enumerate(word):
            self.assertEqual(board.grid[7][7+i].tile, letter)

    def test_put_word_Vertical(self):
        board = Board()
        word = 'CANARIO'
        location = (3,2)
        orientation = 'V'
        board.put_word(word,location,orientation)

        for i, letter in enumerate(word):
            self.assertEqual(board.grid[3+i][2].tile, letter)
    
    def test_put_word_raise(self):
        board = Board()
        word = 'SCRABBLE'
        location = (7,8)
        orientation = 'H'
        with self.assertRaises(InvalidLocation):
            board.put_word(word,location,orientation)

    def test_put_first_word_Horizontal_fine(self):
        board = Board()
        word = 'PERRO'
        location = (7,7)
        orientation = 'H'
        board.put_first_word(word,location,orientation)

        for i, letter in enumerate(word):
            self.assertEqual(board.grid[7][7+i].tile, letter)
    
    def test_put_first_word_vertical_fine(self):
        board = Board()
        word = 'CARPA'
        location = (7,7)
        orientation = 'V'
        board.put_first_word(word,location,orientation)

        for i, letter in enumerate(word):
            self.assertEqual(board.grid[7+i][7].tile, letter)
        
    def test_put_first_word_horizontal_fail(self):
        board = Board()
        word = 'CASA'
        location = (8,3)
        orientation = 'H'
        with self.assertRaises(InvalidLocation):
            board.put_first_word(word,location,orientation)

            
    
    def test_show_board(self):
        board = Board()
        expected_board ="""       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │ Wx3 │     │     │ Lx2 │     │     │     │     │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
        self.assertEqual(expected_board, board.show_board())
    
    def test_show_board_with_word_horizontal(self):
        board = Board()
        word = 'HOLA'
        location = (7,7)
        orientation = 'H'
        board.put_first_word(word, location, orientation)
        expected_board ="""       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │ Wx3 │     │     │ Lx2 │     │     │     │  H  │  O  │  L  │  A  │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
        self.assertEqual(expected_board, board.show_board())



    def test_show_board_with_word_vertical(self):
        board = Board()
        word = 'HOLA'
        location = (7,7)
        orientation = 'V'
        board.put_first_word(word, location, orientation)
        expected_board = """       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │ Wx3 │     │     │ Lx2 │     │     │     │  H  │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │     │     │ Lx2 │     │     │     │ Lx2 │  O  │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │ Lx3 │     │     │     │ Lx3 │     │  L  │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │     │     │     │ Wx2 │     │     │  A  │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
        self.assertEqual(expected_board, board.show_board())

    def test_word_and_multiplier_(self):
        board = Board()
        word = "BIZCOCHO"
        location = (7,7)
        orientation = 'V'
        board.put_word(word, location, orientation)
        expected_board = """       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │ Wx3 │     │     │ Lx2 │     │     │     │  B  │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │     │     │ Lx2 │     │     │     │ Lx2 │  I  │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │ Lx3 │     │     │     │ Lx3 │     │  Z  │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │     │     │     │ Wx2 │     │     │  C  │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │ Lx2 │     │     │ Wx2 │     │     │     │  O  │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │     │     │ Wx2 │     │     │     │ Lx2 │  C  │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │ Wx2 │     │     │     │ Lx3 │     │  H  │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │ Wx3 │     │     │ Lx2 │     │     │     │  O  │     │     │     │ Lx2 │     │     │ Wx3 │
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘"""
        self.assertEqual(expected_board, board.show_board())

                
    def test_words_can_connect_horizontal(self):
        board = Board()
        board.grid[7][7].add_tile(tile=Tile('C', 1))
        board.grid[7][8].add_tile(tile=Tile('A', 1))
        board.grid[7][9].add_tile(tile=Tile('S', 1))
        board.grid[7][10].add_tile(tile=Tile('A', 1))
        word = 'CASCO'
        location = (6,8)
        orientation = 'H'
        word_valid = board.is_word_connected(word, location, orientation)
        self.assertTrue(word_valid)


    def test_placer_word_can_connect_vertical(self):
        board = Board()
        board.grid[7][7].add_tile(tile=Tile('G', 1))
        board.grid[8][7].add_tile(tile=Tile('A', 1))
        board.grid[9][7].add_tile(tile=Tile('T', 1))
        board.grid[10][7].add_tile(tile=Tile('O', 1))
        word = 'MAGO'
        location = (8,6)
        orientation = 'V'
        word_valid = board.is_word_connected(word,location,orientation)
        self.assertTrue(word_valid)

"""
    def test_words_cannot_connect(self):
        board = Board()
        board.grid[7][7].add_tile(tile=Tile('H', 1))
        board.grid[7][8].add_tile(tile=Tile('O', 1))
        board.grid[7][9].add_tile(tile=Tile('L', 1))
        board.grid[7][10].add_tile(tile=Tile('A', 1))
        word = 'PERA'
        location = (6,8)
        orientation = 'H'
        word_valid = board.is_word_connected(word, location, orientation)
        self.assertFalse(word_valid)
"""
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


"""       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │ Wx3 │     │     │ Lx2 │     │     │     │     │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │     │     │ Lx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Lx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │     │     │     │ Wx2 │     │     │     │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │ Lx2 │     │     │ Wx2 │     │     │     │ Lx2 │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
"""