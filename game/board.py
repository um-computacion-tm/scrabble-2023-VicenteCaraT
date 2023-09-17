from game.square import Square

class Board:
    def __init__(self):
        self.grid = [
            [Square(1, '')
             for _ in range(15)]
             for _ in range(15)
        ]
    
    def word_is_valid(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        
        if (orientation == 'H' and x + word_length >= 15) or (orientation == 'V' and y + word_length >= 15):
            return False
        else:
            return True

