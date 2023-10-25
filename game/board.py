from game.square import Square
from game.tile import Tile
from colorama import Fore, Back, Style, init

class InvalidLocation(Exception):
    pass

Wx3 = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
Wx2 = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
Lx3 = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
Lx2 = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class Board:
    def __init__(self): 
        self.grid = [[Square(1, '') for _ in range(15)] for _ in range(15)]
        self.get_multipliers()
        
    def valid_word_in_board(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        
        if (orientation == 'H' and x+ word_length > 15) or (orientation == 'V' and y + word_length > 15):
            return False
        else:
            return True
    
    def valid_word_in_place(self):
        """
        -tendria que chekear si hay suficiente espacio para poner la palabra
        -tendria que chekear si hay alguna letra que se superponga en su camino
        """
        
    def is_empty(self):
        if self.grid[7][7].tile is None:
            return True
        else:
            return False
    
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

    def get_multipliers(self):
        for coordinate in Lx2:
            self.set_multipliers(coordinate, 2, 'letter')
        for coordinate in Lx3:
            self.set_multipliers(coordinate, 3, 'letter')
        for coordinate in Wx2:
            self.set_multipliers(coordinate, 2, 'word')
        for coordinate in Wx3:
            self.set_multipliers(coordinate, 3, 'word')
            
    def set_multipliers(self, coordinate, multiplier, multiplier_type):
        square = self.grid[coordinate[0]][coordinate[1]]
        square.multiplier = multiplier
        square.multiplier_type = multiplier_type
        
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
        
        for i in range(word_length):
            if orientation == 'H':
                cell = self.grid[x][y + i]
            else:
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


    def show_board(self): #Fixing
        spaces = " " * 4
        horizontal_line = spaces + "┌" + "─────┬" * 14 + "─────┐" + "\n"
        middle_horizontal_line = spaces + "├" + "─────┼" * 14 + "─────┤" + "\n"
        bottom_horizontal_line = spaces + "└" + "─────┴" * 14 + "─────┘"

        board = " " * 5 + " ".join([str(i).center(5, " ") for i in range(15)]) + "\n"
        board += horizontal_line

        for i in range(15):
            board += f"{str(i).rjust(3)} │"
            for j in range(15):
                cell = self.grid[i][j]
                if cell.tile is not None:
                    cell_repr = f"{cell.tile}".center(5, " ")
                elif cell.multiplier_type == 'letter':
                    cell_repr = f"Lx{cell.multiplier}".center(5, " ") 
                elif cell.multiplier_type == 'word':
                    cell_repr = f"Wx{cell.multiplier}".center(5, " ")
                else:
                    cell_repr = "     "
                board += cell_repr + "│"
            board += "\n"
            if i != 14:
                board += middle_horizontal_line
        board+= bottom_horizontal_line
        return board
    
