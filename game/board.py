from game.square import Square
from game.tile import Tile

class InvalidLocation(Exception):
    pass

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

    def is_center_empty(self):
        if self.grid[7][7].tile is None:
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
        Lx2 = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
        Lx3 = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
        Wx2 = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
        Wx3 = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

        for row, col in Lx2:
            self.set_multiplier(row, col, 2, 'letter')
        for row, col in Lx3:
            self.set_multiplier(row, col, 3, 'letter')
        for row, col in Wx2:
            self.set_multiplier(row, col, 2, 'word')
        for row, col in Wx3:
            self.set_multiplier(row, col, 3, 'word')

        
    def put_word(self, word, location, orientation):
        x, y = location

        word = word.upper()

        if not self.valid_word_in_board(word, location, orientation):
            raise InvalidLocation('Su palabra no entra en la ubicación')

        if orientation == 'H':
            for index, letter in enumerate(word):
                square = self.grid[x][y + index]
                square.add_tile(str(letter)) 
        if orientation == 'V':
            for index, letter in enumerate(word):
                square = self.grid[x + index][y]
                square.add_tile(str(letter))
    
    def put_first_word(self, word):
        word = word.upper()

        if not self.is_center_empty():
            raise InvalidLocation('La celda central ya está ocupada')
        
        x, y = 7, 7

        if not self.valid_word_in_board(word, (x, y), 'H'):
            raise InvalidLocation('La palabra no se ajusta a la ubicación')
        self.put_word(word, (x, y), 'H')



    def show_board(self):
        board_representation = []
        board_representation.append('  | ' + ''.join([f' {str(col_index).rjust(2)} ' for col_index in range(15)]))
        for row_index, row in enumerate(self.grid):
            row_str = str(row_index).rjust(2) + '| ' + ' '.join([str(cell).rjust(5) for cell in row])
            board_representation.append(row_str)
        return '\n'.join(board_representation)
    """
            
    '''primero definir la posicion de los multiplicadores en listas, por sus respectivos tipos'''
    
    '''def get_multipliers(row,col)'''
    '''def get_multipliers type(row, col)'''


"""

board = Board()
print(board.show_board())
