from game.square import Square

class Board:
    def __init__(self):
        self.grid = [
            [Square(1, '')
             for _ in range(15)]
             for _ in range(15)
        ]
    
'''    def word_is_valid(self, word,position, orientation):
        position_x = position
        position_y = position'''




