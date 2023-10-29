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
        board.grid[7][7] == None
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
        word = 'CASACA'
        location = (12,12)
        orientation = 'H'
        with self.assertRaises(InvalidLocation):
            board.put_first_word(word,location,orientation)

    def test_has_neighgbor_tile_left(self):
        board = Board()
        board.grid[11][3].add_tile(tile=Tile(letter='P', value=1))
        board.grid[12][3].add_tile(tile=Tile(letter='A', value=1))
        board.grid[13][3].add_tile(tile=Tile(letter='S', value=1))
        board.grid[14][3].add_tile(tile=Tile(letter='A', value=1))

        word = 'CASA'
        location = (10, 2)
        orientation = 'V'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor)
    
    def test_has_neighbor_tile_up(self):
        board = Board()
        board.grid[6][1].add_tile(tile=Tile(letter='P', value=1))
        board.grid[7][1].add_tile(tile=Tile(letter='E', value=1))
        board.grid[8][1].add_tile(tile=Tile(letter='L', value=1))
        board.grid[9][1].add_tile(tile=Tile(letter='O', value=1))    

        word = 'MOUSE'
        location = (7,2)
        orientatio = 'V'

        has_neighbor = board.has_neighbor_tile(word,location,orientatio)
        self.assertTrue(has_neighbor) 

    def test_has_neighbor_tile_x2(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='P', value=1))
        board.grid[4][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='L', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='O', value=1))

        board.grid[6][2].add_tile(tile=Tile(letter='C', value=1))
        board.grid[6][3].add_tile(tile=Tile(letter='A', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='A', value=1)) 

        word = 'LAPIZ'
        location = (5, 2)
        orientation = 'V'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor) 

    
    def test_has_neihbor_tile_fail(self):
        board = Board()
        board.grid[6][1].add_tile(tile=Tile(letter='G', value=1))
        board.grid[7][1].add_tile(tile=Tile(letter='O', value=1))
        board.grid[8][1].add_tile(tile=Tile(letter='M', value=1))
        board.grid[9][1].add_tile(tile=Tile(letter='A', value=1))

        word = 'REGLA'
        location = (3,3)
        orientation = 'H'

        has_neighbor = board.has_neighbor_tile(word,location,orientation)
        self.assertFalse(has_neighbor)
    
    def test_has_tile_down_form_word(self):
        board = Board()
        board.grid[5][2].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][3].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='N', value=1))

        word = 'ES'
        location = (5, 6)
        orientation = 'V'

        formed_word = board.find_and_validate_words_up(word, location)
        self.assertTrue(formed_word, 'TRENES')
    

    
    def test_has_tile_up_form_word(self):
      board = Board()
      board.grid[4][3].add_tile(tile=Tile(letter='O', value=1))
      board.grid[4][4].add_tile(tile=Tile(letter='M', value=1))
      board.grid[4][5].add_tile(tile=Tile(letter='A', value=1))

      word = 'G'
      location = (4, 2)
      orientation = 'V'

      formed_word = board.find_and_validate_words_down(word, location)
      self.assertTrue(formed_word, 'GOMA')

        
    
    def test_has_tile_right_form_word(self):
        board = Board()
        board.grid[7][3].add_tile(tile=Tile(letter='J', value=1))
        board.grid[8][3].add_tile(tile=Tile(letter='A', value=1))
        board.grid[9][3].add_tile(tile=Tile(letter='R', value=1))
        board.grid[10][3].add_tile(tile=Tile(letter='O', value=1))

        word = 'PA'
        location = (5,3)
        orientation = 'H'

        formed_word = board.find_and_validate_words_right(word, location)
        self.assertTrue(formed_word, 'PAJARO')
    
    def test_has_tile_left_form_word(self):
        board = Board()
        board.grid[7][3].add_tile(tile=Tile(letter='C', value=1))
        board.grid[8][3].add_tile(tile=Tile(letter='U', value=1))
        board.grid[9][3].add_tile(tile=Tile(letter='D', value=1))
        board.grid[10][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[11][3].add_tile(tile=Tile(letter='R', value=1))   

        word = 'NO'
        location = (9, 4)
        orientation = 'H'

        formed_word = board.find_and_validate_words_left(word, location)   
        self.assertTrue(formed_word, 'CUADERNO')  


    '''
    def test_has_adjacent_word(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][2].add_tile(tile=Tile(letter='S', value=1))
        board.grid[6][2].add_tile(tile=Tile(letter='T', value=1))
        board.grid[7][2].add_tile(tile=Tile(letter='R', value=1))
        board.grid[8][2].add_tile(tile=Tile(letter='E', value=1))
        board.grid[9][2].add_tile(tile=Tile(letter='N', value=1))
        board.grid[10][2].add_tile(tile=Tile(letter='O', value=1))     

        word = 'MES'
        location = (8,1)
        orientation = 'H'

        formed_words = board.find_and_validate_words(word, location, orientation)
        self.assertTrue(formed_words)

    def test_has_adjacent_word_x2(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='C', value=1))
        board.grid[5][2].add_tile(tile=Tile(letter='A', value=1))
        board.grid[6][2].add_tile(tile=Tile(letter='S', value=1))
        board.grid[7][2].add_tile(tile=Tile(letter='A', value=1))

        word = 'S'
        location = (4,6)
        orientation = 'V'

        formed_word = board.find_and_validate_words(word, location, orientation)
        self.assertTrue(formed_word)

    def has_adjacent_word_fail(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='A', value=1))
        board.grid[5][2].add_tile(tile=Tile(letter='P', value=1))
        board.grid[6][2].add_tile(tile=Tile(letter='Q', value=1))
        board.grid[7][2].add_tile(tile=Tile(letter='Z', value=1))

        word = 'X'
        location = (4,6)
        orientation = 'H'

        formed_word = board.find_and_validate_words(word, location, orientation)
        self.assertFalse(formed_word)
    
    def has_adjacent_word_fail_x2(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='X', value=1))
        board.grid[5][2].add_tile(tile=Tile(letter='G', value=1))
        board.grid[6][2].add_tile(tile=Tile(letter='D', value=1))
        board.grid[7][2].add_tile(tile=Tile(letter='W', value=1))

        word = 'XH'
        location = (4, 6)
        orientation = 'V'

        formed_word = board.find_and_validate_words(word, location, orientation)
        self.assertFalse(formed_word)
    '''
    def test_has_crossword(self):
        board = Board()
        board.grid[6][3].add_tile(tile=Tile(letter='P', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='O', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='C', value=1))
        board.grid[6][6].add_tile(tile=Tile(letter='O', value=1))

        word = 'POCA'
        location = (5, 4)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertTrue(has_crossword)
    
    def test_has_crossword_x2(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='P', value=1))
        board.grid[4][3].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='D', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][8].add_tile(tile=Tile(letter='A', value=1))

        board.grid[7][2].add_tile(tile=Tile(letter='M', value=1))
        board.grid[7][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][6].add_tile(tile=Tile(letter='S', value=1))

        word = 'CARAMELO'
        location = (2, 3)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertTrue(has_crossword)

        
    
    def test_has_crossword_fail(self):
        board = Board()
        board.grid[6][3].add_tile(tile=Tile(letter='G', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='O', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='M', value=1))
        board.grid[6][6].add_tile(tile=Tile(letter='A', value=1))  

        word = 'PASO'
        location = (5, 4)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertFalse(has_crossword) 

    def has_crossword_fail_x2(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='P', value=1))
        board.grid[4][3].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='D', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][8].add_tile(tile=Tile(letter='A', value=1))

        board.grid[7][2].add_tile(tile=Tile(letter='M', value=1))
        board.grid[7][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][6].add_tile(tile=Tile(letter='S', value=1))

        word = 'CUADERNO'
        location = (2, 3)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertFalse(has_crossword)



    def test_no_tiles_placed(self):
        board = Board()
        word = 'CINTA'
        location = (5,6)
        orientation = 'V'


        no_tiles = board.no_tiles_placed(word, location, orientation)
        self.assertTrue(no_tiles)

    def test_no_tiles_placed_fail(self):
        board = Board()
        board.grid[6][3].add_tile(tile=Tile(letter='G', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='O', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='M', value=1))
        board.grid[6][6].add_tile(tile=Tile(letter='A', value=1))  

        word = 'COCO'
        location = (4, 5)
        orientation = 'H'

        no_tiles = board.no_tiles_placed(word, location, orientation)
        self.assertFalse(no_tiles)





            
    
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
        self.assertEqual(expected_board, repr(board))
    
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
        self.assertEqual(expected_board, repr(board))



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
        self.assertEqual(expected_board, repr(board))
  

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