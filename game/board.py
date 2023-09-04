from game.square import Square

class Board:
    def __init__(self):
        self.grid = [
            [Square(1, '')
             for _ in range(15)]
             for _ in range(15)
        ]