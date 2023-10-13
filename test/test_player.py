import unittest
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(len(player.playertiles),7)

    def test_reset(self):
        player = Player()
        player.playertiles = [Tile('A', 1),Tile('B', 1), Tile('Ch', 8)]
        player.reset()
        self.assertEqual(len(player.playertiles), 0)
    
    def test_validate_user_has_letters(self):
        player = Player()
        player.playertiles =[
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        word = 'HOLA'
        is_valid = player.has_letter(word)
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        player = Player()
        player.playertiles = [
            Tile(letter='P', value=3),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        word = 'HOLA'
        is_valid = player.has_letter(word)
        self.assertEqual(is_valid, False)

    def test_validate_when_user_has_letter_ch_ll_rr(self):
        player = Player()
        player.playertiles = [
            Tile(letter='C', value=8),
            Tile(letter='O', value=1),
            Tile(letter='C', value=8),
            Tile(letter='L', value=1),
            Tile(letter='H', value=8),
            Tile(letter='O', value=1),
            Tile(letter='M', value=3),
        ]
        word = 'CHOCLO'
        is_valid = player.has_letter(word)
        self.assertEqual(is_valid, True)

class TestPlayer1(unittest.TestCase):

    def test_play_valid_word(self):
        player = Player()
        player.playertiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        word = 'HOLA'
        result = player.play_tiles(word)
        self.assertTrue(result)
        self.assertEqual(len(player.playertiles), 3) 

    def test_play_invalid_word(self):
        player = Player()
        player.playertiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        word = 'CAMA'
        result = player.play_tiles(word)
        self.assertFalse(result)
        self.assertEqual(len(player.playertiles), 7) 
    
