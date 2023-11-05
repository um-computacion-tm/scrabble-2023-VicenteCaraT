import unittest
from game.tile import Tile



class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    
    def test_repr(self):
        tile = Tile ('B', 1)
        expected = "B"
        assert repr(tile) == expected
        
    def test_repr_ch(self):
        tile = Tile ('C', 8)
        expected = "C"
        assert repr(tile) == expected