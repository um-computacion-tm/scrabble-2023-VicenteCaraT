import unittest
from unittest.mock import patch
from game.bagtiles import BagTiles

class TestBagTiles(unittest.TestCase):

    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.total_tiles),103)
        self.assertEqual(patch_shuffle.call_count,1)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.total_tiles,)

    def test_calculate_total(self):
        bag = BagTiles()
        tiles_created = bag.calculate_tiles()
        self.assertEqual(len(tiles_created),103)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(bag.total_tiles), 101)
        self.assertEqual(len(tiles),2)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [('Z', 10),('U', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.total_tiles),105)
    

