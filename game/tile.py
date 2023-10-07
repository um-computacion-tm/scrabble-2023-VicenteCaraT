class Tile:

    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
    
    def __repr__(self): #NEW
        return f"{self.letter}:{self.value}"