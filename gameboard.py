import random
import tile

class GameBoard:

    # GameBoard constructor 
    def __init__(self, num_rows, num_cols, num_mines):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.board = []

    def createBoard(self):
        """
        - create a 2D array of tile objects (num_rows x num_cols) 
        """
        for row in range(self.num_rows):
            self.board.append([]) # add row
            for col in range(self.num_cols):
                self.board[row].append(tile.Tile(row, col)) # add tile objects to each row

    def placeMine(self):
        """
        - randomly place a mine in the game board
        """
        # generate a random row and column to place the mine in
        mine_row = random.randrange(self.num_rows)
        mine_col = random.randrange(self.num_cols)

        # prevent any mines from overlapping
        while (self.board[mine_row][mine_col].isMine()):
            mine_row = random.randrange(self.num_rows)
            mine_col = random.randrange(self.num_cols)
        
        # set the tile to a mine
        self.board[mine_row][mine_col].value = '*'

    def placeMines(self):
        """
        - randomly place mines in the game board
        """
        for mine in range(self.num_mines):
            self.placeMine()

    def fillBoard(self):
        """
        - count the number of mines that touch each tile and assign the tile that value
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):

                if (not self.board[row][col].isMine()):
                    # initialize count for accumulator
                    num_mines_touches = 0

                    # loop through the 8 adjacent tiles
                    for r in range(row - 1, row + 2):
                        for c in range(col - 1, col + 2):
                            # prevent index errors
                            if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):
                                if (self.board[r][c].isMine()):
                                    num_mines_touches += 1

                    # if the tile touches 1 or more mines (not empty), assign the value of the tile to the number of mines it touches
                    if (num_mines_touches != 0):
                        self.board[row][col].value = str(num_mines_touches)
                    else:
                        self.board[row][col].value = ' '

    def clearEmptyCells(self, row, col):
        """
        - flip all of the adjacent empty tiles
        """
        # loop through the 8 adjacent tiles
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                # prevent index errors
                if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols and self.board[r][c].isFlagged == False and self.board[r][c].isMarked == False):
                    # don't repeat the process on cells that are already flipped
                    # this is the base case for the recursion and prevents a max recursion error
                    if (not self.board[r][c].isFlipped):
                        self.board[r][c].flip()
                        # if the adjacent cells are also empty...
                        if (self.board[r][c].isEmpty()):
                            # repeat the process on those cells recursively 
                            self.clearEmptyCells(r, c)

    def revealMines(self):
        """
        - reveal all of the mines
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (self.board[row][col].isMine()):
                    self.board[row][col].flip()

    def guaranteeEmptyCell(self, row, col):
        """
        - guarantee that the user guesses an empty space on the first guess
        """
        while (not self.board[row][col].isEmpty()):
            # loop through the 8 adjacent tiles
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    # prevent index errors
                    if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):
                        while (self.board[r][c].isMine()):
                            # move mine
                            self.board[r][c].value = ' ' 
                            # replace mine
                            self.placeMine()    

            self.fillBoard()

    def hasLost(self, row, col):
        """
        - if the user guesses a mine, return True
        """
        return self.board[row][col].isMine()

    def hasWon(self):
        """ 
        - if the user has flipped every tile that does not contain a mine, return True
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (not (self.board[row][col].isMine() or self.board[row][col].isFlipped)):
                    return False

        return True
