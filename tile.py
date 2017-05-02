class Tile:

    # Tile constructor 
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = ' ' # ' ' is an empty tile
        self.isFlipped = False
        self.isFlagged = False
        self.isMarked = False
        self.count = 0 # tracks how many times tile is clicked for flagging

    def flip(self):
        """
        - set isFlipped to True
        """
        self.isFlipped = True

    def flag(self):
        """
        - set isFlagged to True
        """
        self.isFlagged = True

    def unflag(self):
        """
        - set isFlagged to False
        """
        self.isFlagged = False

    def mark(self):
        """
        - set isMarked to True
        """
        self.isMarked = True

    def unmark(self):
        """
        - set isMarked to False
        """
        self.isMarked = False

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

    def textColor(self):
        """
        - return the right color for each type of tile
        """
        if (self.value == ' '):
            return (200, 200, 200)
        elif (self.value == '1'):
            return (0, 150, 0)
        elif (self.value == '2'):
            return (0, 100, 255)
        elif (self.value == '3'):
            return (255, 0, 0)
        elif (self.value == '4'):
            return (255, 255, 0)
        elif (self.value == '5'):
            return (0, 255, 255)
        elif (self.value == '6'):
            return (255, 0, 255)
        elif (self.value == '7'):
            return (0, 75, 0)
        elif (self.value == '8'):
            return (100, 0, 0)
        elif (self.value == '*'):
            return (255, 0, 0)
