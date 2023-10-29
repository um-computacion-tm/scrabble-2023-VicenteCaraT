class Tile:

    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
           
    def __repr__(self): 
        return f"{self.letter}:{self.value}"