import unittest
from game.square import Square
from game.tile import Tile

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