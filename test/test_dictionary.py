import unittest
from unittest.mock import patch
from game.dictionary import PyraeDict, DictionaryConnectionError

class TestDiccionary(unittest.TestCase):
    @patch('pyrae.dle.search_by_word')
    def test_word_is_in_dictionary(self, mock_is_in_dictionary):
        word = "mes"
        mock_is_in_dictionary.return_value.title = "mes | Definición | Diccionario de la lengua española | RAE - ASALE"
        pyrae_dict = PyraeDict()
        self.assertEqual(pyrae_dict.is_in_dictionary(word), True)
    @patch('pyrae.dle.search_by_word')
    def test_word_not_in_dictionary(self, mock_is_in_dictionary):
        word = "axfsa"
        mock_is_in_dictionary.return_value.title = "Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE"
        pyrae_dict = PyraeDict()
        self.assertEqual(pyrae_dict.is_in_dictionary(word), False)
    @patch('pyrae.dle.search_by_word')
    def test_word_fail(self, mock_is_in_dictionary):
        word = "hola"
        mock_is_in_dictionary.return_value = None
        pyrae_dict = PyraeDict()
        with self.assertRaises(DictionaryConnectionError):
            pyrae_dict.is_in_dictionary(word)


if __name__ == '__main__':
    unittest.main()