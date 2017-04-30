import random       #This module, native to Python, is used for randomly assigning a location in the gameboard to a mine.
import tile         #This module, written by us, is imported here so that Tile objects can be added into the gameboard.

class GameBoard:    #This class designs the gameboard that is to be used in the game of Minesweeper. This class does not display the gameboard. It only describes what it looks like.

    # GameBoard constructor 
    def __init__(self, num_rows, num_cols, num_mines):  #This method asks for the number of rows and columns to be used in the gameboard (which is rectangular), and for the number of mines to be present in this gameboard.
        self.num_rows = num_rows                        #The number of rows in the gameboard.
        self.num_cols = num_cols                        #The nunber of columns in the gameboard.
        self.num_mines = num_mines                      #The number of mines in the gameboard.
        self.board = []                                 #Initializes the array, which represents the gameboard.

    def createBoard(self):
        """
        - create a 2D array of tile objects (num_rows x num_cols) 
        """
        for row in range(self.num_rows):
            self.board.append([]) # add new row        #According to the previously specified number of rows to be used in the gameboard, add that number of empty elements to the previously initialized gameboard. Each element represents a row, so that the board is filled with rows. It is not yet filled with tiles.
            for col in range(self.num_cols):
                self.board[row].append(tile.Tile(row, col)) # add tile objects to each row        #Into each row, add a column of empty tiles. Each tile is indexed by its row and column indices. This completes the array that is the gameboard, and fills the gameboard with empty tiles.

    def placeMine(self):    #For each individual mine to be inserted into the gameboard, this method determines the tile to which the mine is assigned, making sure that no two mines are set to the same tile.
        """
        - randomly place a mine in the game board
        """
        # generate a random row and column to place the mine in
        mine_row = random.randrange(self.num_rows)        #Determine randomly the row index of the mine, corresponding to the row index of a tile.
        mine_col = random.randrange(self.num_cols)        #Determine randomly the column index of the mine, corresponding to the column index of a tile.

        # prevent any mines from overlapping
        while (self.board[mine_row][mine_col].isMine()):    #Ensure that no two mines have the same row and column indices. If the mine of interest is set as having indices already taken by another mine, reassign for the mine of interest these indices randomly.
            mine_row = random.randrange(self.num_rows)
            mine_col = random.randrange(self.num_cols)
        
        # set the tile to a mine
        self.board[mine_row][mine_col].value = '*'    #Set the value of the mine tile to that of a mine, analogously to how the value of an empty cell is set.

    def placeMines(self):    #Execute placeMine() for the total number of mines (already specified) that must be present in the gameboard.
        """
        - randomly place mines in the game board
        """
        for mine in range(self.num_mines):
            self.placeMine()

    def fillBoard(self):    #Assign to each empty tile the value corresponding to the number of adjacent mines.
        """
        - count the number of mines that touch each tile and assign the tile that value
        """
        for row in range(self.num_rows):        #Look at every tile in the gameboard.
            for col in range(self.num_cols):

                if (not self.board[row][col].isMine()):    #A further restriction: look only at empty tiles (tiles that are not mines).

                    # initialize count for accumulator
                    num_mines_touches = 0                #The number of adjacent mines; this number is an accumulator and will be increased during the counting process.

                    # loop through the 8 adjacent tiles
                    for r in range(row - 1, row + 2):        #Look at the indices of both adjacent rows. The variables r and row are numbers (row indices). The second argument of range() is row + 2 because range() has an offset by 1. That is, this function will look at the following indices: row - 1, row + 0, and row + 1.
                        for c in range(col - 1, col + 2):    #Look at the indices of both adjacent columns. The variables c and col are numbers (columns indices). The second argument of range() is col + 2 because range() has an offset by 1. That is, this function will look at the following indices: col - 1, col + 0, and col + 1.
                            # prevent index errors
                            if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):    #A further restriction, to prevent out-of-bounds indexing errors. Of the six indices looked at by the two for loops above, look only at the ones that actually exist in the gameboard.
                                if (self.board[r][c].isMine()):    #All the for loops above ensure that, for each non-mine tile in the gameboard, the counting process looks for mines in the tile itself (which is empty and thus contributes nothing to the accumulator) and in the eights adjacent tiles, if they exist.
                                    num_mines_touches += 1         #Add 1 to the accumulator for each adjacent mine, so that the accumulator ultimately equals the exact number of mines adjacent to the empty tile under examination.

                    # if the tile touches 1 or more mines (not empty), assign the value of the tile to the number of mines it touches
                    if (num_mines_touches != 0):
                        self.board[row][col].value = str(num_mines_touches)    #For each empty tile, set its value as the number of adjacent mines, in the form of text.
                    else:
                        self.board[row][col].value = ' '    #For an empty tile that has zero adjacent mines, its value is the space character, in the form of text.

    #So far, the methods have set up the gameboard, setting all its states before the player has started the game. The following methods concern changes to the states of the gameboard, made by the players.

    def clearEmptyCells(self, row, col):    #This method is to be executed if the player selects an empty tile that is not adjacent to any mine.
        """
        - flip all of the adjacent empty tiles
        """
        # loop through the 8 adjacent tiles
        for r in range(row - 1, row + 2):        #These two for loops and the following if statement have the same purposes that they have in the method fillBoard() above, looking at adjacent tiles.
            for c in range(col - 1, col + 2):
                # prevent index errors
                if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):
                    # don't repeat the process on cells that are already flipped
                    # this is the base case for the recursion and prevents a max recursion error
                    if (not self.board[r][c].isFlipped):        #If the adjacent tile is not flipped, then flip it.
                        self.board[r][c].flip()
                        # if the adjacent cells are also empty...
                        if (self.board[r][c].isEmpty()):        #Furthermore, if the adjacent tile is empty, then recursively execute this entire method for that tile. This flips all contiguous empty tiles.
                            # repeat the process on those cells recursively 
                            self.clearEmptyCells(r, c)

    def revealMines(self):    #Flip every mine in the board. This is only used if the game has ended.
        """
        - reveal all of the mines
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (self.board[row][col].isMine()):
                    self.board[row][col].flip()

    def guaranteeEmptyCell(self, row, col):    #Guarantee that the first tile selected by the player is an empty tile, by moving any mine that happens to be there. The mine is moved by executing the method placeMine(). This method is executed when the player first selects a tile.
        """
        - guarantee that the user guesses an empty space on the first guess
        """
        while (not self.board[row][col].isEmpty()):    #Execute the following code only if the first selected tile is not empty, therefore requiring that the tile be made empty.
            # loop through the 8 adjacent tiles
            for r in range(row - 1, row + 2):        #These two for loops and the following if statement have the same purposes that they have in the method fillBoard() above, looking at adjacent tiles.
                for c in range(col - 1, col + 2):
                    # prevent index errors
                    if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):
                        while (self.board[r][c].isMine()):    #For as long as the first selected tile is a mine, move the mine.
                            # move mine
                            self.board[r][c].value = ' ' 
                            # replace mine
                            self.placeMine()    

            self.fillBoard()    #Update the values of the empty cells because of the new distribution of the mines.

    def hasLost(self, row, col):    #This returns a flag that the user has selected a mine, thereby ending the game. If the player selects a mine, then he cannot have selected every empty tile.
        """
        - if the user guesses a mine, return True
        """
        return self.board[row][col].isMine()

    def hasWon(self):    #This returns a flag that the user has selected every empty tile, thereby winning the game.
        """ 
        - if the user has flipped every tile that does not contain a mine, return True
        """
        for row in range(self.num_rows):    #Look at every tile on the gameboard.
            for col in range(self.num_cols):
                if (not (self.board[row][col].isMine() or self.board[row][col].isFlipped)):    #If even one tile is not a mine and not flipped (i.e. empty and not flipped), then the player has not won yet, though the game is not over.
                    return False

        return True    #If every empty tile has been flipped, then return True, denoting that the player has won the game.

