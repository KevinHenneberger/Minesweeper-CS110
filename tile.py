class Tile:

    # Tile constructor 
    def __init__(self, row, col, value=' ', isFlipped=False):
        self.row = row
        self.col = col
        self.value = value
        self.isFlipped = isFlipped 

    def flip(self):
        """
        - set isFlipped to True
        """
        self.isFlipped = True

    def isMine(self):
        """
        - return if the tile is a mine or not
        """
        return self.value == '*'

    def isEmpty(self):
        """
        - return if the tile is empty or not
        """
        return self.value == ' '

    def display(self):
        """
        - return the tile value
        """
        return self.value
