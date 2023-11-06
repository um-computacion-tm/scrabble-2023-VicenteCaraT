import unittest
from game.board import Board, InvalidLocation
from game.square import Square
from game.tile import Tile
from unittest.mock import patch, Mock
from game.dictionary import PyraeDict


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
    

    def test_word_h_in_board(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.valid_word_in_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_v_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (3, 12)
        orientation = "V"
        word_is_valid = board.valid_word_in_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_v_in_board(self):
        board = Board()
        word = "Facultad"
        location = (1, 12)
        orientation = "V"
        word_is_valid = board.valid_word_in_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_word_h_out_of_board(self):
        board = Board()
        word = 'CELULAR'
        location = (7, 12)
        orientation = 'H'
        word_not_valid = board.valid_word_in_board(word, location, orientation)
        assert word_not_valid == False
    
    def test_word_v_out_of_board(self):
        board = Board()
        word = 'CASCO'
        location = (12, 1)
        orientation = 'V'
        word_not_valid = board.valid_word_in_board(word, location, orientation)
        assert word_not_valid == False
    
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
        location = (3, 5)
        orientation = 'V'

        no_tiles = board.no_tiles_placed(word, location, orientation)
        self.assertFalse(no_tiles)


    def test_board_is_empty(self):
        board = Board()
        board.grid[7][7] == None
        assert board.is_empty() == True
    
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_tile(tile=Tile(letter='C', value=1))
        assert board.is_empty() == False
    


    def test_put_first_word_Horizontal_fine(self):
        board = Board()
        word = 'PERRO'
        location = (7,7)
        orientation = 'H'
        board.put_first_word(word,location,orientation)
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
  7 │ Wx3 │     │     │ Lx2 │     │     │     │  P  │  E  │  R  │  R  │  O  │     │     │ Wx3 │
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
        self.assertEqual(repr(board), expected_board)
        
    def test_put_first_word_horizontal_fail(self):
        board = Board()
        word = 'CASACA'
        location = (12,12)
        orientation = 'H'
        with self.assertRaises(InvalidLocation):
            board.put_first_word(word,location,orientation)

    def test_has_neighbor_tile_h_down(self):
        board = Board()
        board.grid[6][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='A', value=1))

        word = 'CASA'
        location = (5, 4)
        orientation = 'H'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor)
    
    def test_has_neighbor_tile_h_up(self):
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[2][5].add_tile(tile=Tile(letter='E', value=1))
        board.grid[2][6].add_tile(tile=Tile(letter='L', value=1))
        board.grid[2][7].add_tile(tile=Tile(letter='O', value=1))    

        word = 'MOUSE'
        location = (3,5)
        orientation = 'H'

        has_neighbor = board.has_neighbor_tile(word,location,orientation)
        self.assertTrue(has_neighbor) 
    
    def test_has_neighbor_tile_v_left(self):
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='L', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='O', value=1)) 
        board.grid[6][4].add_tile(tile=Tile(letter='L', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='O', value=1))   

        word = 'CAMPERA'
        location = (2,5)
        orientation = 'V'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor)
    
    def has_neighob_tile_v_right(self):
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='C', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='A', value=1)) 
        board.grid[6][4].add_tile(tile=Tile(letter='R', value=1))

        word = 'RADIO'
        location = (3, 2)
        orientation = 'V'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor)

        

    def test_has_neighbor_tile_V_up_down(self):
        board = Board()
        board.grid[4][2].add_tile(tile=Tile(letter='P', value=1))
        board.grid[4][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='L', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='O', value=1))

        board.grid[10][2].add_tile(tile=Tile(letter='C', value=1))
        board.grid[10][3].add_tile(tile=Tile(letter='A', value=1))
        board.grid[10][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[10][5].add_tile(tile=Tile(letter='A', value=1)) 

        word = 'LAPIZ'
        location = (5, 3)
        orientation = 'V'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor) 
    
    def test_has_neighbor_tile_H_right_left(self):
        board = Board()
        board.grid[2][3].add_tile(tile=Tile(letter='C', value=1))
        board.grid[3][3].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][3].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][3].add_tile(tile=Tile(letter='O', value=1))

        board.grid[2][9].add_tile(tile=Tile(letter='C', value=1))
        board.grid[3][9].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][9].add_tile(tile=Tile(letter='O', value=1))
        board.grid[5][9].add_tile(tile=Tile(letter='M', value=1))    
        board.grid[6][9].add_tile(tile=Tile(letter='A', value=1)) 

        word = 'ARROZ'
        location = (4, 4)
        orientation = 'H'

        has_neighbor = board.has_neighbor_tile(word, location, orientation)
        self.assertTrue(has_neighbor)     

    
    def test_has_neihbor_tile_fail(self):
        board = Board()
        board.grid[1][3].add_tile(tile=Tile(letter='G', value=1))
        board.grid[1][4].add_tile(tile=Tile(letter='O', value=1))
        board.grid[1][5].add_tile(tile=Tile(letter='M', value=1))
        board.grid[1][6].add_tile(tile=Tile(letter='A', value=1))

        word = 'REGLA'
        location = (2,9)
        orientation = 'V'

        has_neighbor = board.has_neighbor_tile(word,location,orientation)
        self.assertFalse(has_neighbor)

     
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_tile_down_form_word(self, mock_is_in_dictionary): #patchear dictionary
        board = Board()
        board.grid[1][4].add_tile(tile=Tile(letter='T', value=1))
        board.grid[2][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='N', value=1))

        word = 'ES'
        location = (5, 4)

        is_valid, formed_word = board.find_and_validate_words_up_down(word, location)


        self.assertTrue(is_valid)
        self.assertListEqual(formed_word, ['T','R','E','N'])
        
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_tile_up_form_word(self, mock_is_in_dictionary): #patchear dictionary
      board = Board()
      board.grid[4][6].add_tile(tile=Tile(letter='M', value=1))
      board.grid[5][6].add_tile(tile=Tile(letter='A', value=1))

      word = 'GO'
      location = (2, 6)

      is_valid, formed_word = board.find_and_validate_words_up_down(word, location)

      self.assertTrue(is_valid)
      self.assertListEqual(formed_word, ['M', 'A'])
    
    # fail find_and_validate_words_up_down
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_has_tile_down_fail(self, mock_is_in_dictionary): #patchear dictionary
      board = Board()
      board.grid[1][4].add_tile(tile=Tile(letter='T', value=1))
      board.grid[2][4].add_tile(tile=Tile(letter='R', value=1))
      board.grid[3][4].add_tile(tile=Tile(letter='E', value=1))
      board.grid[4][4].add_tile(tile=Tile(letter='N', value=1))

      word = 'TEST'
      location = (5, 4)
      is_valid= board.find_and_validate_words_up_down(word, location)

      self.assertFalse(is_valid)
    
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_tile_right_form_word(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[3][5].add_tile(tile=Tile(letter='J', value=1))
        board.grid[3][6].add_tile(tile=Tile(letter='A', value=1))
        board.grid[3][7].add_tile(tile=Tile(letter='R', value=1))
        board.grid[3][8].add_tile(tile=Tile(letter='O', value=1))

        word = 'PA'
        location = (3,3)

        formed_word = board.find_and_validate_words_right_left(word, location)
        self.assertTrue(formed_word, 'PAJARO')
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_tile_left_form_word(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[7][3].add_tile(tile=Tile(letter='P', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='L', value=1))

        word = 'A'
        location = (7, 6)

        formed_word = board.find_and_validate_words_right_left(word, location)   
        self.assertTrue(formed_word, 'PALA')  
    
    # fail find_and_validate_word_right_left
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_has_tile_right_fail(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[7][3].add_tile(tile=Tile(letter='P', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='L', value=1))

        word = 'X'
        location = (7, 2)

        formed_word = board.find_and_validate_words_right_left(word, location)
        self.assertFalse(formed_word)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_word(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[5][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][6].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][8].add_tile(tile=Tile(letter='N', value=1))
        board.grid[5][9].add_tile(tile=Tile(letter='O', value=1))    

        word = 'MES'
        location = (4, 7)

        formed_words_list = ['ME', 'EN', 'SO']

        formed_words = board.find_and_validate_words_adjacent_horizontal(word, location)
        self.assertTrue(formed_words, formed_words_list)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_3words_down(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[8][5].add_tile(tile=Tile(letter='R', value=1))
        board.grid[9][5].add_tile(tile=Tile(letter='U', value=1))
        board.grid[10][5].add_tile(tile=Tile(letter='J', value=1))
        board.grid[11][5].add_tile(tile=Tile(letter='O', value=1))

        board.grid[8][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[9][4].add_tile(tile=Tile(letter='M', value=1))
        board.grid[10][4].add_tile(tile=Tile(letter='A', value=1))


        board.grid[8][8].add_tile(tile=Tile(letter='R', value=1))
        board.grid[9][8].add_tile(tile=Tile(letter='O', value=1))
        board.grid[10][8].add_tile(tile=Tile(letter='S', value=1))  

        word = 'CABEZA'
        location = (7, 3)

        formed_word_list = ['BRUJO', 'ARMA', 'AROS']
        
        formed_words = board.find_and_validate_words_adjacent_horizontal(word, location)
        self.assertTrue(formed_words, formed_word_list)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_3word_up(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][4].add_tile(tile=Tile(letter='C', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='S', value=1))
        
        board.grid[2][6].add_tile(tile=Tile(letter='B', value=1))
        board.grid[3][6].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][6].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][6].add_tile(tile=Tile(letter='I', value=1))

        board.grid[4][9].add_tile(tile=Tile(letter='A', value=1))
        board.grid[5][9].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][9].add_tile(tile=Tile(letter='T', value=1))  

        word = 'BILLETE'
        location = (7, 3)

        formed_word_list = ['CASI', 'BARRIL', 'ARTE']

        formed_words = board.find_and_validate_words_adjacent_horizontal(word, location)
        self.assertTrue(formed_words, formed_word_list)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_word_down(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[5][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][6].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][8].add_tile(tile=Tile(letter='N', value=1))
        board.grid[5][9].add_tile(tile=Tile(letter='O', value=1))

        word = 'MES'
        location = (6, 7)

        formed_words_list = ['ME', 'EN', 'SO']

        formed_word = board.find_and_validate_words_adjacent_horizontal(word, location)
        self.assertTrue(formed_word, formed_words_list)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_3word_right(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='G', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='L', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='A', value=1))


        board.grid[6][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='P', value=1))
        board.grid[6][6].add_tile(tile=Tile(letter='A', value=1))
        board.grid[6][7].add_tile(tile=Tile(letter='C', value=1))
        board.grid[6][8].add_tile(tile=Tile(letter='I', value=1))
        board.grid[6][9].add_tile(tile=Tile(letter='O', value=1))


        board.grid[8][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[8][5].add_tile(tile=Tile(letter='M', value=1))
        board.grid[8][6].add_tile(tile=Tile(letter='A', value=1))

        word = 'CARPETA'
        location = (2, 3)

        formed_word_list = ['REGLA', 'ESPACIO', 'ARMA']

        formed_word = board.find_and_validate_words_adjacent_vertical(word, location)
        self.assertTrue(formed_word, formed_word_list)

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_3word_left(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][6].add_tile(tile=Tile(letter='D', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='O', value=1))

        board.grid[6][5].add_tile(tile=Tile(letter='C', value=1))
        board.grid[6][6].add_tile(tile=Tile(letter='H', value=1))
        board.grid[6][7].add_tile(tile=Tile(letter='A', value=1))

        board.grid[9][3].add_tile(tile=Tile(letter='B', value=1))
        board.grid[9][4].add_tile(tile=Tile(letter='L', value=1))
        board.grid[9][5].add_tile(tile=Tile(letter='A', value=1))
        board.grid[9][6].add_tile(tile=Tile(letter='N', value=1))
        board.grid[9][7].add_tile(tile=Tile(letter='C', value=1))

        word = 'MOSQUITO'
        location = (2, 8)

        formed_word_list = ['DOS', 'CHAU', 'BLANCO']

        formed_words = board.find_and_validate_words_adjacent_vertical(word, location)
        self.assertTrue(formed_words, formed_word_list)

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_has_adjacent_word_left(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='N', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='O', value=1))

        word = 'MES'       
        location = (6, 5)

        formed_word_list = ['ME', 'EN', 'SO']

        formed_word = board.find_and_validate_words_adjacent_vertical(word, location)
        self.assertTrue(formed_word, formed_word_list)     
    
    # Adjacent Fails
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_adjacente_H_fail(self, mock_is_in_dictionary): #patchar dictionary
        board = Board() 
        board.grid[6][4].add_tile(tile=Tile(letter='Q', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='X', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='P', value=1))

        board.grid[6][5].add_tile(tile=Tile(letter='H', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='J', value=1))

        board.grid[6][6].add_tile(tile=Tile(letter='K', value=1))
        board.grid[7][6].add_tile(tile=Tile(letter='T', value=1))

        word = 'MAGO'
        location = (5, 3)

        formed_word_fail = board.find_and_validate_words_adjacent_horizontal(word, location)
        self.assertFalse(formed_word_fail)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_adjacent_V_fail(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[3][4].add_tile(tile=Tile(letter='X', value=1))
        board.grid[3][5].add_tile(tile=Tile(letter='Q', value=1))

        board.grid[5][4].add_tile(tile=Tile(letter='H', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='J', value=1))

        board.grid[6][3].add_tile(tile=Tile(letter='N', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='Z', value=1)) 
        board.grid[6][5].add_tile(tile=Tile(letter='X', value=1))

        word = 'MAGIA'
        location = (2, 6)

        formed_word_fail = board.find_and_validate_words_adjacent_vertical(word, location)
        self.assertFalse(formed_word_fail)
    
    def test_has_crossword(self):
        board = Board()
        board.grid[2][6].add_tile(tile=Tile(letter='P', value=1))
        board.grid[3][6].add_tile(tile=Tile(letter='O', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='C', value=1))
        board.grid[5][6].add_tile(tile=Tile(letter='O', value=1))

        word = 'POCA'
        location = (3, 5)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertTrue(has_crossword)
    
    def test_has_crossword_x2(self):
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='D', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='A', value=1))

        board.grid[2][7].add_tile(tile=Tile(letter='M', value=1))
        board.grid[3][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='S', value=1))
        board.grid[5][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[6][7].add_tile(tile=Tile(letter='S', value=1))

        word = 'CARAMELO'
        location = (3, 2)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertTrue(has_crossword)

        
    
    def test_has_crossword_fail(self):
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='G', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='O', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='M', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='A', value=1))  

        word = 'PASO'
        location = (3, 3)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertFalse(has_crossword) 

    def has_crossword_fail_x2(self):
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='D', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='A', value=1))

        board.grid[2][7].add_tile(tile=Tile(letter='M', value=1))
        board.grid[3][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='S', value=1))
        board.grid[5][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[6][7].add_tile(tile=Tile(letter='S', value=1))

        word = 'CUADERNO'
        location = (3, 2)
        orientation = 'H'

        has_crossword = board.has_crossword(word, location, orientation)
        self.assertFalse(has_crossword)
    
    def test_get_word_cells_horizontal(self):
        board = Board()
        word = 'TEST'
        location = (3, 3)
        orientation = 'H'

        word_cells = board.get_word_cells(word, location, orientation)

        expected_word_cells = [board.grid[3][3], board.grid[3][4], board.grid[3][5], board.grid[3][6]]
        self.assertListEqual(word_cells, expected_word_cells)

    def test_get_word_cells_vertical(self):
        board = Board()
        word = 'TEST'
        location = (3, 3)
        orientation = 'V'

        word_cells = board.get_word_cells(word, location, orientation)
        
        expected_word_cells = [board.grid[3][3], board.grid[4][3], board.grid[5][3], board.grid[6][3]]
        self.assertListEqual(word_cells, expected_word_cells)

            
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
      
    
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_crossword(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[2][5].add_tile(tile=Tile(letter='A', value=1))
        board.grid[3][5].add_tile(tile=Tile(letter='B', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='J', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='A', value=1))

        word = 'ABEJORRO'
        location = (3, 4)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_invalid_corssword(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[2][5].add_tile(tile=Tile(letter='P', value=1))
        board.grid[3][5].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='O', value=1))

        word = 'CAJA'
        location = (3, 4)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_formed_word_adjacent_horizontal(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[5][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][6].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][8].add_tile(tile=Tile(letter='N', value=1))
        board.grid[5][9].add_tile(tile=Tile(letter='O', value=1))

        word = 'MES'
        location = (6, 7)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_no_formed_word_adjacent_horizontal(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[5][3].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][6].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][7].add_tile(tile=Tile(letter='E', value=1))
        board.grid[5][8].add_tile(tile=Tile(letter='N', value=1))
        board.grid[5][9].add_tile(tile=Tile(letter='O', value=1))

        word = 'XYZ'
        location = (4, 4)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_formed_word_right(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][5].add_tile(tile=Tile(letter='N', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='O', value=1))

        word = 'MA'
        location = (4, 3)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_word_formed_left(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[3][3].add_tile(tile=Tile(letter='G', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='O', value=1))
        board.grid[3][5].add_tile(tile=Tile(letter='R', value=1))

        word = 'RO'
        location = (3, 6)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_no_formed_word_right(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][4].add_tile(tile=Tile(letter='C', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='P', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='A', value=1))

        word = 'TRE'
        location = (4, 1)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_no_formed_word_left(self, mock_is_in_dictionary): #patchar dictionary
        board = Board() 
        board.grid[4][2].add_tile(tile=Tile(letter='C', value=1))
        board.grid[4][3].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[4][6].add_tile(tile=Tile(letter='E', value=1))
        board.grid[4][7].add_tile(tile=Tile(letter='R', value=1))
        board.grid[4][8].add_tile(tile=Tile(letter='O', value=1))

        word = 'PO'
        location = (4, 9)
        orientation = 'H'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_word_formed_adjacent_vertical(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='N', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='O', value=1))

        word = 'MES'       
        location = (6, 5)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_no_formed_word_adjacent_vertical(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='S', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='T', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='N', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='O', value=1))   

        word = 'YZQ'
        location = (6, 5)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)   
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_formed_word_up(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[2][4].add_tile(tile=Tile(letter='C', value=1))
        board.grid[3][4].add_tile(tile=Tile(letter='A', value=1))
        board.grid[4][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='E', value=1))

        word = 'TA'
        location = (7, 4)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)   

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_valid_word_with_formed_word_down(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][4].add_tile(tile=Tile(letter='P', value=1))
        board.grid[5][4].add_tile(tile=Tile(letter='I', value=1))
        board.grid[6][4].add_tile(tile=Tile(letter='C', value=1))
        board.grid[7][4].add_tile(tile=Tile(letter='E', value=1))
        board.grid[8][4].add_tile(tile=Tile(letter='R', value=1))
        board.grid[9][4].add_tile(tile=Tile(letter='A', value=1))

        word = 'LA'
        location = (2, 4)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertTrue(result)

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_no_word_formed_up(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[4][5].add_tile(tile=Tile(letter='B', value=1))
        board.grid[5][5].add_tile(tile=Tile(letter='U', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='Z', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='O', value=1))

        word = 'PON'
        location = (8, 5)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result) 
    

    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_word_with_no_word_formed_down(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[5][5].add_tile(tile=Tile(letter='F', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='O', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[8][5].add_tile(tile=Tile(letter='O', value=1))

        word = 'SAPO'
        location = (9, 5)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)
    
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = False)
    def test_valid_no_neighbor_tile(self, mock_is_in_dictionary): #patchar dictionary
        board = Board()
        board.grid[5][5].add_tile(tile=Tile(letter='F', value=1))
        board.grid[6][5].add_tile(tile=Tile(letter='O', value=1))
        board.grid[7][5].add_tile(tile=Tile(letter='T', value=1))
        board.grid[8][5].add_tile(tile=Tile(letter='O', value=1))

        word = 'SANTO'
        location = (5, 9)
        orientation = 'V'

        result = board.valid_word_in_place(word, location, orientation)
        self.assertFalse(result)



class TestCalculateWordValue(unittest.TestCase):

    def test_calculate_word(self):
        board = Board()
        word = [
            Square(tile=Tile('C', 3)),
            Square(tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 6)

    def test_with_letter_multiplier(self):
        board = Board()
        word = [
            Square(multiplier=2, multiplier_type='letter', tile=Tile('C', 3)),
            Square(tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 9)

    def test_with_word_multiplier(self):
        board = Board()
        word = [
            Square(multiplier=2, multiplier_type='word', tile=Tile('C', 3)),
            Square(tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]

        value = board.calculate_word_value(word)
        self.assertEqual(value, 12)

    def test_with_letter_word_multiplier(self):
        board = Board()
        word = [
            Square(multiplier=3, multiplier_type='letter', tile=Tile('C', 3)),
            Square(multiplier=2, multiplier_type= 'word', tile=Tile('A', 1)),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 24)

    def test_with_letter_word_multiplier_no_active(self):
        board = Board()
        word = [
            Square(multiplier=2, multiplier_type='word', tile=Tile('C', 3), active=False),
            Square(multiplier=3, multiplier_type= 'letter', tile=Tile('A', 1), active=True),
            Square(tile=Tile('S', 1)),
            Square(tile=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 8)

