import unittest
from game.scrabbleGame import (ScrabbleGame, InvalidPlaceWordException, InvalidWordException, InvalidWordNoLetters)
from game.tile import Tile
from game.board import Board
from game.player import Player
from unittest.mock import patch, Mock, MagicMock

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
    
    def test_get_current_player(self):
        # Crear un juego con 3 jugadores
        scrabble_game = ScrabbleGame(total_players=3)

        scrabble_game.next_turn()

        scrabble_game.get_current_player()
        self.assertEqual(scrabble_game.current_player.id, 0)

        scrabble_game.next_turn()

        scrabble_game.get_current_player()
        self.assertEqual(scrabble_game.current_player.id, 1)
        
    def test_is_playing(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.bag_tiles.total_tiles = [Tile('A', 1), Tile('B', 3)]
        self.assertTrue(scrabble_game.is_playing())
    def test_is_playing_no_more_tiles(self):
        scrabble_game = ScrabbleGame(total_players=3)
        scrabble_game.bag_tiles.total_tiles = []
        self.assertFalse(scrabble_game.is_playing())
    
    def test_round_set(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        player = scrabble_game.current_player
        initial_tile_count = len(player.playertiles)
        scrabble_game.round_set()
        new_tile_count = len(player.playertiles)
        self.assertEqual(new_tile_count, 7 - initial_tile_count)  # Verificar que se han añadido las fichas adecuadas

    def test_start_game(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        player = scrabble_game.current_player
        initial_tile_count = len(scrabble_game.current_player.playertiles)
        scrabble_game.start_game()
        new_tile_count = len(player.playertiles)
        self.assertEqual(new_tile_count, 7 - initial_tile_count)

    def test_validate_word_has_letter_raise(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.board.grid[7][7].add_tile(Tile(letter='P', value=1))
        scrabble_game.board.grid[7][8].add_tile(Tile(letter='I', value=1))
        scrabble_game.board.grid[7][9].add_tile(Tile(letter='Z', value=1))
        scrabble_game.board.grid[7][10].add_tile(Tile(letter='Z', value=1))
        scrabble_game.board.grid[7][11].add_tile(Tile(letter='A', value=1))       
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles =[
            Tile(letter='V', value=1),
            Tile(letter='A', value=1),
            Tile(letter='L', value=1),
            Tile(letter='I', value=1),
            Tile(letter='D', value=1),
            Tile(letter='O', value=1),
        ]

        word = 'VACA'
        location = (5, 7)
        orientation = 'H'


        with self.assertRaises(InvalidWordNoLetters):
            scrabble_game.validate_word(word, location, orientation)
    '''
    def test_validate_word_is_in_dictionary_raise(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles=[
            Tile(letter='X', value=1),
            Tile(letter='C', value=1),
            Tile(letter='S', value=1),
            Tile(letter='I', value=1),
            Tile(letter='F', value=1),
            Tile(letter='Q', value=1),
        ]

        word = 'XCS'
        location = (7, 2)
        orientation = 'V'

        with self.assertRaises(InvalidWordException):
            scrabble_game.validate_word(word, location, orientation)
      '''
    def test_validate_word_in_board(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles= [
            Tile(letter='P', value=1),
            Tile(letter='I', value=1),
            Tile(letter='S', value=1),
            Tile(letter='O', value=1),
            Tile(letter='F', value=1),
            Tile(letter='Q', value=1),
        ]
        word = 'PISO'
        location = (8, 12)
        orientation = 'H'

        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word(word, location, orientation)
    
    def test_validate_word_in_place_raise(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.board.grid[7][7].add_tile(Tile(letter='G', value=1))
        scrabble_game.board.grid[7][8].add_tile(Tile(letter='E', value=1))
        scrabble_game.board.grid[7][9].add_tile(Tile(letter='N', value=1))
        scrabble_game.board.grid[7][10].add_tile(Tile(letter='T', value=1))
        scrabble_game.board.grid[7][11].add_tile(Tile(letter='E', value=1))
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles=[
            Tile(letter='P', value=1),
            Tile(letter='E', value=1),
            Tile(letter='R', value=1),
            Tile(letter='R', value=1),
            Tile(letter='O', value=1),
            Tile(letter='O', value=1),          
        ]

        word = 'PERRO'
        location = (7, 2)
        orientation = 'H'

        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word(word, location, orientation)
    
    def test_validate_word_increse_round(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.board.grid[7][7].add_tile(Tile(letter='G', value=1))
        scrabble_game.board.grid[7][8].add_tile(Tile(letter='E', value=1))
        scrabble_game.board.grid[7][9].add_tile(Tile(letter='N', value=1))
        scrabble_game.board.grid[7][10].add_tile(Tile(letter='T', value=1))
        scrabble_game.board.grid[7][11].add_tile(Tile(letter='E', value=1))
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles =[
            Tile(letter='P', value=1),
            Tile(letter='E', value=1),
            Tile(letter='S', value=1),
            Tile(letter='R', value=1),
            Tile(letter='O', value=1),
            Tile(letter='O', value=1),    
        ] 

        word = 'PESO'
        location = (6, 8)
        orientation = 'V'

        self.assertEqual(scrabble_game.round, 1)
        scrabble_game.validate_word(word, location, orientation)
        self.assertEqual(scrabble_game.round, 1)
    
    def test_valid_word_first_round_has_tile_raise(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles = [
            Tile(letter='Z', value=1),
            Tile(letter='X', value=1),
            Tile(letter='S', value=1),
            Tile(letter='R', value=1),
            Tile(letter='O', value=1),
            Tile(letter='S', value=1),   
        ]

        word = 'ORO'
        location = (7, 7)
        orientation = 'H'

        with self.assertRaises(InvalidWordNoLetters):
            scrabble_game.validate_word_first_round(word, location, orientation)
    
    def test_valid_word_first_round_is_in_dinctionary_raise(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles = [
            Tile(letter='X', value=1),
            Tile(letter='O', value=1),
            Tile(letter='R', value=1),
            Tile(letter='R', value=1),
            Tile(letter='O', value=1),
            Tile(letter='S', value=1),  
        ]

        word = 'XORR'
        location = (7, 7)
        orientation = 'H'

        with self.assertRaises(InvalidWordException):
            scrabble_game.validate_word_first_round(word, location, orientation)
    
    def test_valid_word_first_round_valid_word_in_board(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles = [
            Tile(letter='P', value=1),
            Tile(letter='E', value=1),
            Tile(letter='R', value=1),
            Tile(letter='R', value=1),
            Tile(letter='A', value=1),
            Tile(letter='O', value=1),  
        ]

        word = 'PERO'
        location = (12, 7)
        orientation = 'V'

        with self.assertRaises(InvalidPlaceWordException):
            scrabble_game.validate_word_first_round(word, location, orientation)

    def test_valid_word_first_round_round(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles = [
            Tile(letter='P', value=1),
            Tile(letter='E', value=1),
            Tile(letter='R', value=1),
            Tile(letter='C', value=1),
            Tile(letter='A', value=1),
            Tile(letter='H', value=1),  
        ]

        word = 'PERCHA'
        location = (7, 7)
        orientation = 'V'

        self.assertEqual(scrabble_game.round, 1)
        scrabble_game.validate_word_first_round(word, location, orientation)
        self.assertEqual(scrabble_game.round, 1)

    def test_play_fist_word(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles = [
            Tile(letter='P', value=1),
            Tile(letter='E', value=1),
            Tile(letter='R', value=1),
            Tile(letter='C', value=1),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),  

        ]

        word = 'PESCAR'
        location = (7, 7)
        orientation = 'H'

        scrabble_game.play_first_round(word, location, orientation)

        self.assertEqual(len(scrabble_game.current_player.playertiles), 0)

        expexted_board ="""       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
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
  7 │ Wx3 │     │     │ Lx2 │     │     │     │  P  │  E  │  S  │  C  │  A  │  R  │     │ Wx3 │
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
        
        self.assertEqual(repr(scrabble_game.board), expexted_board)

    def test_play(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        scrabble_game.current_player.playertiles = [
            Tile(letter='P', value=1),
            Tile(letter='E', value=1),
            Tile(letter='Z', value=1),

        ]
        
        word = 'PEZ'
        location = (3, 7)
        orientation = 'V'

        scrabble_game.play(word, location, orientation)

        self.assertEqual(len(scrabble_game.current_player.playertiles), 0)

        expected_board ="""       0     1     2     3     4     5     6     7     8     9     10    11    12    13    14 
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  0 │ Wx3 │     │     │ Lx2 │     │     │     │ Wx3 │     │     │     │ Lx2 │     │     │ Wx3 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  1 │     │ Wx2 │     │     │     │ Lx3 │     │     │     │ Lx3 │     │     │     │ Wx2 │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │     │ Wx2 │     │     │     │ Lx2 │     │ Lx2 │     │     │     │ Wx2 │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │ Lx2 │     │     │ Wx2 │     │     │     │  P  │     │     │     │ Wx2 │     │     │ Lx2 │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │     │     │     │     │ Wx2 │     │     │  E  │     │     │ Wx2 │     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │ Lx3 │     │     │     │ Lx3 │     │  Z  │     │ Lx3 │     │     │     │ Lx3 │     │
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
        
        self.assertEqual(repr(scrabble_game.board), expected_board)
      
    def test_has_joker_current_player(self):
        game = ScrabbleGame(total_players=2)
        game.next_turn()
        game.current_player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3)
        ]
        result = game.has_joker_current_player()
        self.assertTrue(result)

    def test_convert_joker_to_letter(self):
        game = ScrabbleGame(total_players=2)
        game.next_turn()
        game.current_player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3)
        ]
        game.convert_joker_to_letter('C')

        self.assertEqual(game.current_player.playertiles[1].letter, 'C')
        self.assertEqual(game.current_player.playertiles[1].value, 0)

    def test_get_joker_index(self):
        game = ScrabbleGame(total_players=2)
        game.next_turn()
        game.current_player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='?', value=0),
            Tile(letter='B', value=3)
        ]
        index = game.get_joker_index()
        self.assertEqual(index, 1)

    def test_get_valid_letter_input(self):
        # Simula una entrada de usuario válida
        with unittest.mock.patch('builtins.input', return_value='C'):
            game = ScrabbleGame(total_players=2)
            game.next_turn()  # Llama a next_turn antes de obtener la entrada del usuario
            letter = game.get_valid_letter_input()
            self.assertEqual(letter, 'C')

        # Simula una entrada de usuario no válida (número en lugar de letra)
        with unittest.mock.patch('builtins.input', return_value='1'):
            game = ScrabbleGame(total_players=2)
            game.next_turn()  # Llama a next_turn antes de obtener la entrada del usuario
            with self.assertRaises(ValueError):
                game.get_valid_letter_input()

        # Simula una entrada de usuario no válida (más de una letra)
        with unittest.mock.patch('builtins.input', return_value='AB'):
            game = ScrabbleGame(total_players=2)
            game.next_turn()  # Llama a next_turn antes de obtener la entrada del usuario
            with self.assertRaises(ValueError):
                game.get_valid_letter_input()

        # Simula una entrada de usuario no válida (letra minúscula)
        with unittest.mock.patch('builtins.input', return_value='a'):
            game = ScrabbleGame(total_players=2)
            game.next_turn()  # Llama a next_turn antes de obtener la entrada del usuario
            letter = game.get_valid_letter_input()
            self.assertEqual(letter, 'A')