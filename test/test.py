import unittest
from game.model import (
    BagTiles,
    Tile,
)
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
            bag.tiles,
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

if __name__ == '__main__':
    unittest.main()