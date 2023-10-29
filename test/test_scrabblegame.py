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

    def test_next_turn_round(self):
        # Arrange
        total_players = 3
        scrabble_game = ScrabbleGame(total_players=2)

        # Act
        current_player, round_number = scrabble_game.next_turn()

        # Assert
        expected_round_number = 2  # Se espera que la ronda se incremente a 2 después de la primera llamada a next_turn
        self.assertEqual(round_number, expected_round_number, "La ronda no se incrementa correctamente.")

        # Act nuevamente para verificar si la ronda sigue aumentando
        current_player, round_number = scrabble_game.next_turn()

        # Assert
        expected_round_number = 3  # Se espera que la ronda se incremente a 3 después de la segunda llamada a next_turn
        self.assertEqual(round_number, expected_round_number, "La ronda no se incrementa correctamente en el segundo turno.")
'''
    def test_get_current_player(self):
        # Crear un juego con 3 jugadores
        scrabble_game = ScrabbleGame(total_players=3)

        # Verificar que al principio el jugador actual es el jugador 0
        scrabble_game.get_current_player()
        self.assertEqual(scrabble_game.current_player.id, None)

        # Avanzar al siguiente turno
        scrabble_game.next_turn()

        # Verificar que ahora el jugador actual es el jugador 1
        scrabble_game.get_current_player()
        self.assertEqual(scrabble_game.current_player.id, 0)

        # Avanzar al siguiente turno
        scrabble_game.next_turn()

        # Verificar que ahora el jugador actual es el jugador 2
        scrabble_game.get_current_player()
        self.assertEqual(scrabble_game.current_player.id, 1)

        # Avanzar al siguiente turno (vuelve al primer jugador)
        scrabble_game.next_turn()

        # Verificar que ahora el jugador actual es nuevamente el jugador 0
        scrabble_game.get_current_player()
        self.assertEqual(scrabble_game.current_player.id, 0)
        '''
'''
    def test_exchange_tiles(self):
        scrabble_game = ScrabbleGame(total_players=2)
        scrabble_game.next_turn()
        initial_tiles = scrabble_game.current_player.playertiles = [
            Tile(letter='A', value=1),
            Tile(letter='B', value=1),
            Tile(letter='C', value=1),
            Tile(letter='D', value=1),
            Tile(letter='E', value=1),
            Tile(letter='F', value=1)
        ]  # Configurar las fichas del jugador

        # Índices de las fichas que se intercambiarán
        tiles_to_exchange_indices = [1, 3, 5]  # Por ejemplo, intercambiar las fichas en las posiciones 1, 3 y 5

        # Intercambiar las fichas y obtener las fichas intercambiadas
        exchanged_tiles = scrabble_game.exchange_tiles(tiles_to_exchange_indices)

        # Verificar que las fichas intercambiadas estén en la bolsa de fichas
        for tile in exchanged_tiles:
            self.assertIn(tile, scrabble_game.bag_tiles.total_tiles)

        # Verificar que las fichas originales del jugador estén de vuelta en la bolsa de fichas
        for index in tiles_to_exchange_indices:
            self.assertNotIn(initial_tiles[index - 1], scrabble_game.current_player.playertiles)
            '''