from game.square import Square
from game.tile import Tile

class InvalidLocation(Exception):
    pass

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
                    #multiplier= get_multipliers(row,col),
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
        

    def get_multipliers(self,row,col): #Fixing

        Lx2 = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
        Lx3 = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
        Wx2 = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
        Wx3 = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

        for a in Lx2:
            self.grid[a[row]][a[col]] = Square(multiplier=2, multiplier_type='letter')
            repr(Square().multiplier)
        for b in Lx3:
            self.grid[b[row]][b[col]] = Square(multiplier=3, multiplier_type='letter')
            repr(Square().multiplier)
        for c in Wx2:
            self.grid[c[row]][c[col]] = Square(multiplier=2, multiplier_type='word')
            repr(Square().multiplier)
        for d in Wx3:
            self.grid[d[row]][d[col]] = Square(multiplier=3, multiplier_type='word')
            repr(Square().multiplier)
        
    def put_word(self,word,location,orientation): #New
        x, y = location

        if not self.valid_word_in_board(word, location, orientation):
            raise InvalidLocation('Su palabra no entra en la ubicación')
        
        if orientation == 'H':
            for index,letter in word:
                self.grid[x][y+index].add_tile(letter)
        if orientation == 'V':
            for index, letter in word:
                self.grid[x+index][y].add_letter(letter)

    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
            
    '''primero definir la posicion de los multiplicadores en listas, por sus respectivos tipos'''
    
    '''def get_multipliers(row,col)'''
    '''def get_multipliers type(row, col)'''


