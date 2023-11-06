
from pyrae import dle

class DictionaryConnectionError(Exception):
    ...
dle.set_log_level(log_level='CRITICAL') 

class PyraeDict:

    def is_in_dictionary(self, word):
            searchResult = dle.search_by_word(word)

            if searchResult == None:
                raise DictionaryConnectionError("No fue ingresada una palabra o el servicio está caído.")
            
            failMessage = "Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE"
            return searchResult.title != failMessage