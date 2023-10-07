from game.square import Square
from game.tile import Tile

class Board:
    def __init__(self, fill_with=" " * (15*15)): 
        self.grid = [
            [
                Square(
                    tile=(
                        Tile(
                            letter=fill_with[(row * 15)+col], value=1
                        ) 
                        if fill_with[(row * 15)+col] != " " 
                        else None
                    ),
                )
                for col in range(15)
            ]
            for row in range(15)
        ]
        
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
    
    def show_board(board): #NEW
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
        )

    def place_word_in_board(word, location, orientation):
        pass



        
    '''primero definir la posicion de los multiplicadores en listas, por sus respectivos tipos'''
    
    '''def get_multipliers(row,col)'''
    '''def get_multipliers type(row, col)'''

board = Board()
print(board.show_board())