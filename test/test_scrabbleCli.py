import unittest
from unittest.mock import patch, Mock, call, MagicMock
from io import StringIO
from game.scrabbleCli import ScrabbleCli
from game.dictionary import PyraeDict


class TestCLI(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        cli = ScrabbleCli()
        self.assertEqual(
            cli.get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        cli = ScrabbleCli()
        self.assertEqual(
            cli.get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '2'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        cli = ScrabbleCli()
        self.assertEqual(
            cli.get_player_count(),
            2,
        )

    @patch('builtins.print')
    def test_welcome_message(self, mock_print):
        cli = ScrabbleCli()
        cli.welcome_message()
        calls = [
            unittest.mock.call("--------------------------------------------------------------------------------------------"),
            unittest.mock.call("------------------------------Welcome to Scrabble by Vicente--------------------------------"),
            unittest.mock.call("--------------------------------------------------------------------------------------------")
        ]
        mock_print.assert_has_calls(calls)
    
    @patch('builtins.print')
    def test_show_game_options(self, mock_print):
        cli = ScrabbleCli()
        cli.scrabble = Mock()
        cli.scrabble.board = "Test Board"
        cli.scrabble.get_current_player.return_value = "Player 1"
        cli.show_game_options()
        calls = [
            unittest.mock.call("----------------------------------------Scrabble Board-----------------------------------------"),
            unittest.mock.call("Test Board"),
            unittest.mock.call("-------------------------------------------Options---------------------------------------------"),
            unittest.mock.call("Press 1 to Put Word"),
            unittest.mock.call("Press 2 to Change your Tiles"),
            unittest.mock.call("Press 3 to Change all your Tiles"),
            unittest.mock.call("Press 4 to Pass Turn"),
            unittest.mock.call("Press 5 to End the Game"),
            unittest.mock.call("Press 6 to Convert Joker"),
            unittest.mock.call("Press 7 to See all Valid Moves in this ScrabbleGame"),
            unittest.mock.call("-----------------------------------------------------------------------------------------------"),
            unittest.mock.call("Player 1")
        ]
        mock_print.assert_has_calls(calls)
    
    @patch('builtins.input', return_value='PERRO')
    def test_get_word_input_valid(self, mock_input):
        cli = ScrabbleCli()
        word = cli.get_word_input()
        self.assertEqual(word, 'PERRO')
    
    @patch('builtins.input', side_effect=['145', 'PERRO'])
    @patch('builtins.print')
    def test_get_word_input_invalid_and_valid(self, mock_print, mock_input):
        cli = ScrabbleCli()
        with patch('builtins.input', side_effect=['145', 'PERRO']):
            word = cli.get_word_input()
            self.assertEqual(word, 'PERRO')
            mock_print.assert_called_once_with("Invalid word. Please enter alphabetic characters only.")
    
    @patch('builtins.input', side_effect=['7', '7'])
    def test_get_coordinates_valid(self, mock_input):
        cli = ScrabbleCli()
        coordinates = cli.get_coordinates()
        self.assertEqual(coordinates, (7, 7))

    @patch('builtins.input', side_effect=['invalid', 'abc', '1', '2'])
    @patch('builtins.print')
    def test_get_coordinates_invalid_then_letter_then_valid(self, mock_print, mock_input):
        cli = ScrabbleCli()
        with patch('builtins.input', side_effect=['invalid', 'abc', '1', '2']):
            coordinates = cli.get_coordinates()
            self.assertEqual(coordinates, (1, 2))
            mock_print.assert_has_calls([
                unittest.mock.call("Invalid input. Please enter valid numbers for coordinates."),
                unittest.mock.call("Invalid input. Please enter valid numbers for coordinates.")
            ])
    
    @patch('builtins.input', side_effect=['ROPA', '7', '7', 'H'])
    @patch('builtins.print')
    @patch.object(PyraeDict, 'is_in_dictionary', return_value = True)
    def test_handle_user_input_option_1(self, mock_print, mock_input, mock_is_in_dictionary): #patchar dictionary
        cli = ScrabbleCli()
        cli.scrabble = Mock() 
        cli.scrabble.round = 1
        cli.handle_user_input(1)
        cli.scrabble.validate_word_first_round.assert_called_once_with('ROPA', (7, 7), 'H')
        cli.scrabble.play_first_round.assert_called_once_with('ROPA', (7, 7), 'H')
        cli.scrabble.round_set.assert_called_once()
        cli.scrabble.round +=1

    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    @patch.object(ScrabbleCli, 'get_word_input', return_value="CARPA")
    @patch.object(ScrabbleCli, 'get_coordinates', return_value=(5, 2))
    @patch.object(ScrabbleCli, 'get_orientation', return_value='V') 
    def test_handle_user_input_option_1_else(self, mock_get_orientation, mock_get_coordinates, mock_get_word_input, mock_print, mock_input): #patchar dictionary
        cli = ScrabbleCli()
        cli.scrabble = Mock()
        cli.scrabble.round = 2 

        cli.handle_user_input(1) 

        mock_get_word_input.assert_called_once()
        mock_get_coordinates.assert_called_once()
        mock_get_orientation.assert_called_once()

        cli.scrabble.validate_word.assert_called_once_with("CARPA", (5, 2), 'V')
        cli.scrabble.play.assert_called_once_with("CARPA", (5, 2), 'V')
        cli.scrabble.round_set.assert_called_once()

        mock_print.assert_not_called()
        mock_input.assert_not_called()
    
    @patch('builtins.input', side_effect=['2', '2, 3'])
    @patch('builtins.print')
    def test_handle_user_input_option_2(self, mock_print, mock_input):
        cli = ScrabbleCli()
        cli.scrabble = Mock()

        expected_tiles = [Mock(), Mock()]
        cli.scrabble.exchange_tiles.return_value = expected_tiles

        cli.handle_user_input(2)

        cli.scrabble.exchange_tiles.assert_called_once_with([2])

        mock_print.assert_called_with("Exchanged tiles: ", expected_tiles)
        mock_input.assert_has_calls([call("Enter the indices of tiles you want to exchange (comma-separated): ")])
    
    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print') 
    def test_handle_user_input_option_3(self, mock_print, mock_input):
        cli = ScrabbleCli()
        cli.scrabble = Mock()

        expected_tiles = [Mock(), Mock(), Mock()]
        cli.scrabble.exchange_all_tiles.return_value = expected_tiles

        cli.handle_user_input(3)

        cli.scrabble.exchange_all_tiles.assert_called_once()

        mock_print.assert_has_calls([
            call('Okay, exchanging all your tiles'),
            call("Exchanged tiles: ", expected_tiles)
        ])

    @patch('builtins.input', side_effect=['4'])
    @patch('builtins.print') 
    def test_handle_user_input_option_4(self, mock_print, mock_input):
        cli = ScrabbleCli()
        cli.scrabble = Mock()

        cli.handle_user_input(4)

        cli.scrabble.next_turn.assert_called_once()

        mock_print.assert_called_once_with("Well, passing to the next player...")

        mock_input.assert_not_called()


    ''' #fix
    @patch('builtins.input', side_effect=['2', '1', '1,2,3', 'invalid', '3', '4', '5'])
    @patch('game.scrabbleCli.ScrabbleCli.welcome_message')
    @patch('game.scrabbleCli.ScrabbleCli.get_player_count', return_value=2)
    @patch('game.scrabbleCli.ScrabbleCli.show_game_options')
    @patch('game.scrabbleCli.ScrabbleCli.handle_user_input')
    def test_client(self, mock_handle_input, mock_show_options, mock_get_player_count, mock_welcome_message, mock_input):
        cli = ScrabbleCli()
        cli.client()

        mock_welcome_message.assert_called_once()
        mock_get_player_count.assert_called_once()
        mock_show_options.assert_called()
        mock_handle_input.assert_called()
    '''

    @patch('builtins.input', side_effect=['quit'])
    @patch('builtins.print')
    def test_handle_option_7(self, mock_print, mock_input):
        cli = ScrabbleCli()
        cli.scrabble = Mock()
        cli.valid_1 = Mock()
        cli.valid_2 = Mock()
        cli.handle_option_7()
        cli.valid_1.assert_called_once()
        cli.valid_2.assert_called_once()
        mock_input.assert_called_once_with("Enter any letter to exit the validations: ")
        mock_print.assert_called_once_with("Exiting validations...")
    
    @patch('builtins.input', return_value='x')
    @patch('builtins.print')
    def test_handle_option_7_called_from_handle_user_input(self, mock_print, mock_input):
        with patch.object(ScrabbleCli, 'valid_1') as mock_valid_1, \
            patch.object(ScrabbleCli, 'valid_2') as mock_valid_2:
            cli = ScrabbleCli()

            cli.handle_user_input(7)

            mock_valid_1.assert_called_once()  
            mock_valid_2.assert_called_once()  
            mock_input.assert_called_once_with("Enter any letter to exit the validations: ") 
            mock_print.assert_called_once_with("Exiting validations...")

    @patch('builtins.input', side_effect=['A', '1', 'H'])
    def test_handle_option_6(self, mock_input):
        cli = ScrabbleCli()
        cli.scrabble.current_player.has_joker = MagicMock(return_value=True)
        cli.scrabble.get_valid_letter_input = MagicMock(return_value='H')
        cli.handle_option_6()
        cli.scrabble.convert_joker_to_letter.assert_called_once_with('H')

    @patch('builtins.input', side_effect=['A', '1', 'H'])
    def test_handle_option_6(self, mock_input):
        cli = ScrabbleCli()
        cli.scrabble = MagicMock()
        cli.scrabble.current_player.has_joker = MagicMock(return_value=True)
        cli.scrabble.get_valid_letter_input = MagicMock(return_value='H')
        cli.handle_option_6()
        cli.scrabble.convert_joker_to_letter.assert_called_once_with('H')