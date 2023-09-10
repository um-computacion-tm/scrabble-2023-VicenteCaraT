from game.square import Square

class Board:
    def __init__(self):
        self.grid = [
            [Square(1, '')
             for _ in range(15)]
             for _ in range(15)
        ]
    
    def word_is_valid(self, word, location, orientation):
        if orientation == 'H' and (location[0] + len(word)) >= 15:
            return False
        elif orientation == 'V' and (location[1] + len(word)) >= 15:
            return False
        else:
            return True




