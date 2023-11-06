import unittest
from game.player import Player
from game.bagtiles import BagTiles
from game.tile import Tile
from game.board import Board

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(len(player.playertiles),0)

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
        result = player.play_word(word)
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
        result = player.play_word(word)
        self.assertFalse(result)
        self.assertEqual(len(player.playertiles), 7) 
        
    def test_get_tiles(self):
        player = Player()
        initial_tile_count = len(player.bag_tiles.total_tiles)
        count = 7

        player.get_tiles(player.bag_tiles, count)

        self.assertEqual(len(player.playertiles), count)
        self.assertEqual(len(player.bag_tiles.total_tiles), initial_tile_count - count)

    def test_score_update(self):
        player = Player()
        self.assertEqual(player.score, 0)
        score = 72
        player.score_update(score)
        self.assertEqual(player.score, score)

    def test_show_tiles_plyer_atril(self):
        player = Player()
        player.id = 2
        player.score = 23
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
            Tile(letter='A', value=1),
        ]
        expected_output = (
            "Player ID: 2\n"
            "Score: 23\n"
            "Atril: A:1 | A:1 | A:1 | A:1 | A:1 | A:1 | A:1 |\n"
            "indx:    1     2     3     4     5     6     7"
        )
        # Eliminar espacios en blanco al final de las cadenas antes de comparar
        self.assertMultiLineEqual(player.show_tiles().strip(), expected_output.strip())
    
    def test_player_repr(self):
        player = Player()
        player.id = 0
        player.score = 100
        player.playertiles= [
            Tile(letter='B', value=1),
            Tile(letter='B', value=1),
            Tile(letter='B', value=1),
            Tile(letter='B', value=1),
            Tile(letter='B', value=1),
            Tile(letter='B', value=1),
            Tile(letter='B', value=1),
        ]
        expected_output = (
            "Player ID: 0\n"
            "Score: 100\n"
            "Atril: B:1 | B:1 | B:1 | B:1 | B:1 | B:1 | B:1 |\n"
            "indx:    1     2     3     4     5     6     7"
        )
        self.assertMultiLineEqual(repr(player).strip(), expected_output.strip())

    def test_has_joker_with_joker(self):
        player = Player()
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3),
        ]
        has_joker = player.has_joker()
        self.assertTrue(has_joker)

    def test_has_joker_without_joker(self):
        player = Player()
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='B', value=3),
            Tile(letter='C', value=3),
        ]
        has_joker = player.has_joker()
        self.assertFalse(has_joker)

    def test_convert_joker_to_letter(self):
        player = Player()
        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3),
            Tile(letter='C', value=3),
        ]

        player.convert_joker_to_letter('D')
        self.assertEqual(player.playertiles[1].letter, 'D')
        self.assertEqual(player.playertiles[1].value, 0)

        with self.assertRaises(Exception) as context:
            player.convert_joker_to_letter('E')
        self.assertEqual(
            str(context.exception), "Player does not have a Joker in their tiles.")

        player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='B', value=3),
            Tile(letter='C', value=3),
        ]
        with self.assertRaises(Exception) as context:
            player.convert_joker_to_letter('E')
        self.assertEqual(
            str(context.exception), "Player does not have a Joker in their tiles.")