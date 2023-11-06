from game.square import Square
from game.tile import Tile
from game.dictionary import PyraeDict

class InvalidLocation(Exception):
    pass
class InvalidWord(Exception):
    pass
SCRABBLE_LETTER_VALUES = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'L': 1, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 5,
    'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Y': 4, 'Z': 10
}
Wx3 = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
Wx2 = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
Lx3 = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
Lx2 = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class Board:
    def __init__(self): 
        self.grid = [[Square(1, '') for _ in range(15)] for _ in range(15)]
        self.get_multipliers()
        self.dict = PyraeDict()


    def valid_word_in_place(self, word, location, orientation):
        if not self.no_tiles_placed(word, location, orientation):
            if self.has_crossword(word, location, orientation):
                return True
        else:
            if self.has_neighbor_tile(word, location, orientation):
                if orientation == 'H' or orientation == 'h':
                    return self.find_and_validate_words_adjacent_horizontal(word, location) or self.find_and_validate_words_right_left(word, location)
                else:
                    return self.find_and_validate_words_adjacent_vertical(word, location) or self.find_and_validate_words_up_down(word, location)
            return False

        
    def valid_word_in_board(self, word, location, orientation):
        row, col = location
        word_length = len(word)
        
        if (orientation == 'H' and col + word_length > 15) or (orientation == 'V' and row + word_length > 15):
            return False
        else:
            return True
    
    def no_tiles_placed(self, word, location, orientation):
        row, col = location
        for i in range(len(word)):
            check_row, check_col = (row, col + i) if orientation == 'H' else (row + i, col)
            if 0 <= check_row < 15 and 0 <= check_col < 15 and self.grid[check_row][check_col].tile:
                return False 
        return True  
       
    def has_neighbor_tile(self, word, location, orientation):
        row, col = location
        word_length = len(word)
        neighbors_list = []

        for i in range(word_length):
            if orientation == 'H':
                neighbors_positions = [(row - 1, col + i), (row + 1, col + i), (row, col + i - 1), (row, col + i + 1)]
            else:  # orientation == 'V'
                neighbors_positions = [(row + i - 1, col), (row + i + 1, col), (row + i, col - 1), (row + i, col + 1)]

            for pos in neighbors_positions:
                row_pos, col_pos = pos
                if 0 <= row_pos < 15 and 0 <= col_pos < 15:
                    neighbor_tile = self.grid[row_pos][col_pos].tile
                    if neighbor_tile:
                        neighbors_list.append((pos, neighbor_tile.letter))

        return neighbors_list


    # fijarce si las 4 funciones se pueden hacer en 1
    def find_and_validate_words_up_down(self, word, location): #test para False y lista
        row, col = location
        formed_word = []
        if self.grid[row][col].tile:
            formed_word.append(self.grid[row][col].tile.letter)
        
        # Iterar hacia arriba
        current_row, current_col = row - 1, col 
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.insert(0, self.grid[current_row][current_col].tile.letter)
            current_row -= 1

        # Iterar hacia abajo
        current_row, current_col = row + len(word), col
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.append(self.grid[current_row][current_col].tile.letter)
            current_row += 1

        formed_word_str = ''.join(formed_word)
        formed_word_str_down = word + formed_word_str
        formed_word_str_up = formed_word_str + word
        if self.dict.is_in_dictionary(formed_word_str_up) or self.dict.is_in_dictionary(formed_word_str_down):
            return True, formed_word
        else:
            return False
        
    def find_and_validate_words_right_left(self, word, location): # arreglar el iterar hacia la izquierda, test para lista y false
        row, col = location
        formed_word = []
        if self.grid[row][col].tile:
            formed_word.append(self.grid[row][col].tile.letter)

        # Iterar hacia la izquierda
        current_row, current_col = row, col - 1
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.insert(0, self.grid[current_row][current_col].tile.letter)
            current_col -= 1

        # Iterar hacia la derecha
        current_row, current_col = row, col + len(word)
        while self.is_valid_position((current_row, current_col)) and self.grid[current_row][current_col].tile:
            formed_word.append(self.grid[current_row][current_col].tile.letter)
            current_col += 1

        formed_word_str = ''.join(formed_word)
        formed_word_str_left = formed_word_str + word
        formed_word_str_right = word + formed_word_str
        if self.dict.is_in_dictionary(formed_word_str_left) or self.dict.is_in_dictionary(formed_word_str_right):
            return True, formed_word
        else:
            return False
    
    def find_and_validate_words_adjacent_horizontal(self, word, location):
        row, col = location
        formed_words = []

        for i, letter in enumerate(word):
            formed_word = [letter]
            current_row, current_col = row, col

            # Iterar hacia arriba
            while self.is_valid_position((current_row - 1, current_col)) and self.grid[current_row - 1][current_col].tile:
                current_row -= 1
                formed_word.insert(0, self.grid[current_row][current_col].tile.letter)

            current_row, current_col = row, col

            # Iterar hacia abajo
            while self.is_valid_position((current_row + 1, current_col)) and self.grid[current_row + 1][current_col].tile:
                current_row += 1
                formed_word.append(self.grid[current_row][current_col].tile.letter)

            formed_word_str = ''.join(formed_word)
            if len(formed_word_str) > 1 and self.dict.is_in_dictionary(formed_word_str):
                formed_words.append(formed_word_str)
            elif len(formed_word_str) > 1 and not self.dict.is_in_dictionary(formed_word_str):
                return False

            col += 1

        return formed_words
    

    def find_and_validate_words_adjacent_vertical(self, word, location):
        row, col = location
        formed_words = []

        for i, letter in enumerate(word):
            formed_word = [letter]
            current_row, current_col = row, col

            # Iterar hacia la izquierda
            while self.is_valid_position((current_row , current_col - 1)) and self.grid[current_row][current_col - 1].tile:
                current_col -= 1
                formed_word.insert(0, self.grid[current_row][current_col].tile.letter)

            current_row, current_col = row, col

            # Iterar hacia la derecha
            while self.is_valid_position((current_row , current_col + 1)) and self.grid[current_row ][current_col + 1].tile:
                current_col += 1
                formed_word.append(self.grid[current_row][current_col].tile.letter)

            formed_word_str = ''.join(formed_word)
            if len(formed_word_str) > 1 and self.dict.is_in_dictionary(formed_word_str):
                formed_words.append(formed_word_str)
            elif len(formed_word_str) > 1 and not self.dict.is_in_dictionary(formed_word_str):
                return False

            row += 1

        return formed_words

    def is_valid_position(self, position):
        row, col = position
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])


    def has_crossword(self, word, location, orientation):
        row, col = location       
        for i, letter in enumerate(word):
            cross_row, cross_col = (row, col + i) if orientation == 'H' else (row + i, col)

            if self.grid[cross_row][cross_col].tile:
                existing_tile = self.grid[cross_row][cross_col].tile                
                if existing_tile.letter != letter:
                    return False
        return True
    
    
    def calculate_word_value(self, word): #testear y arreglar
        total_value = 0
        word_multiplier = 1

        for square in word:
            if square.tile:
                letter_value = SCRABBLE_LETTER_VALUES.get(square.tile.letter.upper(), 0)
                if square.multiplier_type == 'letter' and square.active:
                    total_value += letter_value * square.multiplier
                elif square.multiplier_type == 'word' and square.active:
                    total_value += letter_value
                    word_multiplier *= square.multiplier
                else:
                    total_value += letter_value

        total_value *= word_multiplier
        return total_value

    def is_empty(self):
        if self.grid[7][7].tile is None:
            return True
        else:
            return False   
        
    def put_word(self, word, location, orientation):
        x, y = location
        word_cells = []

        for i, letter in enumerate(word):
            if orientation == 'H':
                cell = self.grid[x][y + i]
            else:
                cell = self.grid[x + i][y]

            # Obtén el valor de la letra desde el diccionario
            letter_value = SCRABBLE_LETTER_VALUES.get(letter, 0)
            tile = Tile(letter=letter, value=letter_value)
            cell.add_tile(tile)
            word_cells.append(cell)

        return word_cells
    def get_word_cells(self, word, location, orientation): #testear
        word_cells = [] 
        row, col = location 

        for letter in word:
            word_cells.append(self.grid[row][col])  
            if orientation.upper() == 'H':
                col += 1  
            else:
                row += 1  

        return word_cells #testear
    
    def put_first_word(self, word, location, orientation):
        x, y = 7,7

        if location != (x, y):
            raise InvalidLocation('La primera palabra tiene que ser colocada en la posición (7,7)')
        else:
            self.put_word(word, location, orientation)

    def get_multipliers(self):
        for coordinate in Lx2:
            self.set_multipliers(coordinate, 2, 'letter')
        for coordinate in Lx3:
            self.set_multipliers(coordinate, 3, 'letter')
        for coordinate in Wx2:
            self.set_multipliers(coordinate, 2, 'word')
        for coordinate in Wx3:
            self.set_multipliers(coordinate, 3, 'word')
            
    def set_multipliers(self, location, multiplier, multiplier_type):
        square = self.grid[location[0]][location[1]]
        square.multiplier = multiplier
        square.multiplier_type = multiplier_type

    def __repr__(self): #Fixing
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
                    cell_repr = f"{cell.tile.letter}".center(5, " ")
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
