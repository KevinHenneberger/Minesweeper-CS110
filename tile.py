class Tile:    #This class describes the tiles that are to be used in the game of Minesweeper. A tile is a placeholder for either a mine, or emptiness (not holding a mine).

    # Tile constructor 
    def __init__(self, row, col):    #This method asks for the row and column indices of the tile.
        self.row = row               #The row index of the tile.
        self.col = col               #The column index of the tile.
        self.value = ' '             #The tile is empty (i.e. there is no mine beneath it). This value can be changed so that there is a mine beneath the tile (i.e. '*'). A tile is either a single mine or is empty. If the tile is empty, then either no number is displayed on it when it has been flipped (if it is not adjacent to a mine), or a number is displayed on it when it has been flipped, denoting the number of mines to which the tile is adjacent. The adjacent mine tiles do not have to have been flipped for their mines to factor into the number displayed on the empty tile.
        self.isFlipped = False       #This is a Boolean value denoting whether the tile has been flipped. By default, tiles are not flipped. They are flipped when a player selects them or when the game ends.
        self.isFlagged = False       #This is a Boolean value denoting whether the tile has been flagged by the player (indicating that the tile has a mine beneath it).
        self.isMarked = False        #This is a Boolean value denoting whether the tile has been marked (indicating that the tile has an unknown entity beneath it).
        self.count = 0               #This is the number of times that the right mouse button has been pressed. This value may be changed to allow for a larger number of presses. This variable is used for flagging tiles, marking tiles, and resetting tiles to their default state.

    def flip(self):                  #Flip the tile so that its value becomes known to the player.
        """
        - set isFlipped to True
        """
        self.isFlipped = True

    def flag(self):                  #Flag the tile.
        """
        - set isFlagged to True
        """
        self.isFlagged = True

    def unflag(self):                #Unflag the tile.
        """
        - set isFlagged to False
        """
        self.isFlagged = False

    def mark(self):                  #Mark the tile.
        """
        - set isMarked to True
        """
        self.isMarked = True

    def unmark(self):                #Unmark the tile.
        """
        - set isMarked to False
        """
        self.isMarked = False

    def isMine(self):                #Set the value of the tile as being a mine tile. There is a mine below the tile.
        """
        - return if the tile is a mine or not
        """
        return self.value == '*'

    def isEmpty(self):               #Set the value of the tile as being an empty tile. There is not a mine below the tile.
        """
        - return if the tile is empty or not
        """
        return self.value == ' '

    def textColor(self):             #This sets the color of the text on the flipped empty tile. The text denotes the number of mines to which the flipped tile is adjacent.
        """
        - return the right color for each type of tile
        """
        if (self.value == ' '):      #The empty tile is adjacent to zero mines. The text on the flipped tile is a space character, and its color is purest white.
            return (200, 200, 200)
        elif (self.value == '1'):    #The empty tile is adjacent to one mine only. The text on the flipped tile denotes this number, one, and its color is green.
            return (0, 150, 0)
        elif (self.value == '2'):    #Two mines adjacent. Its color is blue.
            return (0, 100, 255)
        elif (self.value == '3'):    #Three mines adjacent. Its color is red.
            return (255, 0, 0)
        elif (self.value == '4'):    #Four mines adjacent. Its color is yellow.
            return (255, 255, 0)
        elif (self.value == '5'):    #Five mines adjacent. Its color is light blue.
            return (0, 255, 255)
        elif (self.value == '6'):    #Six mines adjacent. Its color is pink.
            return (255, 0, 255)
        elif (self.value == '7'):    #Seven mines adjacent. Its color is dark green.
            return (0, 75, 0)
        elif (self.value == '8'):    #Eight mines adjacent. Its color is dark red. Due to geometric constraints, eight is the maximum possible number of tiles, and therefore mines, adjacent to a tile.
            return (100, 0, 0)
        elif (self.value == '*'):    #This tile is not an empty tile. It is, instead, a mine tile. The text displayed is an asterisk, which is displayed when the tile has been flipped. The color of the text is red.
            return (255, 0, 0)

