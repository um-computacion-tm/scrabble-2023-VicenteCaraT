from game.square import Square
from game.tile import Tile

class InvalidLocation(Exception):
    pass

LX2 = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
Lx3 = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
Wx2 = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
Wx3 = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

class Board:
    def __init__(self): 
        self.grid = [[Square(1, '')for _ in range(15)]for _ in range(15)]
        
    def valid_word_in_board(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        
        if (orientation == 'H' and x+ word_length >= 15) or (orientation == 'V' and y + word_length >= 15):
            return False
        else:
            return True
        
    def is_empty(self):
        for row in self.grid:
            for square in row:
                if square.tile is not None:
                    return False
        return True
    
    @staticmethod
    def calculate_word_score(word:list[Square]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_letter_score()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value
    

    def set_multiplier(self, row, col, multiplier, multiplier_type):
        square = self.grid[row][col]
        square.multiplier = multiplier
        square.multiplier_type = multiplier_type

    def get_multipliers(self,row,col): #Fixing

        for row, col in LX2:
            self.set_multiplier(row, col, multiplier=2, multiplier_type='letter')
        for row, col in Lx3:
            self.set_multiplier(row, col, multiplier=3, multiplier_type='letter')
        for row, col in Wx2:
            self.set_multiplier(row, col, multiplier=2, multiplier_type='word')
        for row, col in Wx3:
            self.set_multiplier(row, col, multiplier=3, multiplier_type='word')

        
    def put_word(self, word, location, orientation):
        x, y = location

        if not self.valid_word_in_board(word, location, orientation):
            raise InvalidLocation('Su palabra no entra en la ubicación')

        if orientation == 'H':
            for index, letter in enumerate(word.upper()):
                square = self.grid[x][y + index]
                square.add_tile(letter) 
        if orientation == 'V':
            for index, letter in enumerate(word.upper()):
                square = self.grid[x + index][y]
                square.add_tile(letter)
    
    def put_first_word(self, word, location, orientation):
        x, y = 7,7

        if location != (x, y):
            raise InvalidLocation('La primera palabra tiene que ser colocada en la posición (7,7)')

        elif not self.valid_word_in_board(word, (x, y), orientation):
            raise InvalidLocation('La palabra no puede ser colocada en la posición (7,7) con la orientación especificada')
        
        self.put_word(word, (x, y), orientation)
    
    def is_word_connected(self, word, location, orientation):  #FIXING
        x, y = location
        word_length = len(word)

        if not self.valid_word_in_board(word, location, orientation):
            return False

        # Verificar las letras cruzadas
        for i in range(word_length):
            if orientation == 'H':
                cell = self.grid[x][y + i]
            else:  # orientation == 'V'
                cell = self.grid[x + i][y]

            if cell.tile is not None and cell.tile.letter != word[i]:
                return False
            if orientation == 'V' and x + i + 1 < 15:
                cross_cell = self.grid[x + i + 1][y]
                if cross_cell.tile is not None and cross_cell.tile.letter != word[i]:
                    return False
            if orientation == 'H' and y + i + 1 < 15:
                cross_cell = self.grid[x][y + i + 1] 
                if cross_cell.tile is not None and cross_cell.tile.letter != word[i]:
                    return False
        return True


    def show_board(self):
        pass



    
    """
            
    '''primero definir la posicion de los multiplicadores en listas, por sus respectivos tipos'''
    
    '''def get_multipliers(row,col)'''
    '''def get_multipliers type(row, col)'''


"""

