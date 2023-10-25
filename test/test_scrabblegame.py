import unittest
from game.scrabbleGame import ScrabbleGame
from game.tile import Tile
from game.board import Board

class TestScrabblePlayers(unittest.TestCase):

    def test_init_scrabble(self):
        scrabble_game = ScrabbleGame(total_players= 4)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),4)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]  
    
    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]
    
    def test_first_round_set(self):
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.fist_round_set()
        for player in scrabble_game.players:
            self.assertEqual(len(player.playertiles), 7)
    
    def test_game_over(self):
        scrable_game = ScrabbleGame(total_players=2)
        scrable_game.bag_tiles.total_tiles = []       
        self.assertTrue(scrable_game.game_over())
        scrable_game.bag_tiles.total_tiles = [
            Tile('A', 1),
            Tile('B', 1)
        ]
        self.assertFalse(scrable_game.game_over())