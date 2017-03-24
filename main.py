# import libraries
import random

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

class GameBoard:

    # GameBoard constructor 
    def __init__(self, num_rows, num_cols, num_mines, game_board=[]):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_mines = num_mines
        self.game_board = game_board

    def createBoard(self):
        """
        - create a 2D array of tile objects (num_rows x num_cols) 
        """
        for row in range(self.num_rows):
            self.game_board.append([]) # add new row
            for col in range(self.num_cols):
                self.game_board[row].append(Tile(row, col)) # add tile objects to each row

    def placeMine(self):
        """
        - randomly place a mine in the game board
        """
        # generate a random row and column to place the mine in
        mine_row = random.randrange(self.num_rows)
        mine_col = random.randrange(self.num_cols)

        # prevent any mines from overlapping
        while (self.game_board[mine_row][mine_col].isMine()):
            mine_row = random.randrange(self.num_rows)
            mine_col = random.randrange(self.num_cols)
        
        # set the tile to a mine
        self.game_board[mine_row][mine_col].value = '*'

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

                if (not self.game_board[row][col].isMine()):

                    # initialize count for accumulator
                    num_mines_touches = 0

                    # loop through the 8 adjacent tiles
                    for r in range(row - 1, row + 2):
                        for c in range(col - 1, col + 2):
                            # prevent index errors
                            if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):
                                if (self.game_board[r][c].isMine()):
                                    num_mines_touches += 1

                    # if the tile touches 1 or more mines (not empty), assign the value of the tile to the number of mines it touches
                    if (num_mines_touches != 0):
                        self.game_board[row][col].value = str(num_mines_touches)
                    else:
                        self.game_board[row][col].value = ' '

    def clearEmptyCells(self, row, col):
        """
        - flip all of the adjacent empty tiles
        """
        # loop through the 8 adjacent tiles
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                # prevent index errors
                if (r >= 0 and c >= 0 and r < self.num_rows and c < self.num_cols):
                    # don't repeat the process on cells that are already flipped
                    # this is the base case for the recursion and prevents a max recursion error
                    if (not self.game_board[r][c].isFlipped):
                        self.game_board[r][c].flip()
                        # if the adjacent cells are also empty...
                        if (self.game_board[r][c].isEmpty()):
                            # repeat the process on those cells recursively 
                            self.clearEmptyCells(r, c)

    def revealMines(self):
        """
        - reveal all of the mines
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (self.game_board[row][col].isMine()):
                    self.game_board[row][col].flip()

    def hasLost(self, row, col):
        """
        - if the user guesses a mine, return True
        """
        return self.game_board[row][col].isMine()

    def hasWon(self):
        """
        - if the user has flipped every tile that does not contain a mine, return True
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (not (self.game_board[row][col].isMine() or self.game_board[row][col].isFlipped)):
                    return False

        return True

    def lostGame(self):
        """
        - lost game function
        """
        self.revealMines()
        self.displayBoard()
        print("GAME OVER!")

    def wonGame(self):
        """
        - won game function
        """
        self.displayBoard()
        print('YOU WON!')

    def displayBoard(self):
        """
        - print the properly formatted game board to the console
        """
        for row in range(self.num_rows):
            print('|', end='')
            for col in range(self.num_cols):
                if (self.game_board[row][col].isFlipped):
                    print(self.game_board[row][col].display(), end='|')
                else:
                    print('#', end='|')
            print('')

    def gameLoop(self):
        """
        - run a continuous game loop that prompts the user to guess tiles until the game ends (user wins or loses)
        """
        # setup the game board
        self.createBoard()
        self.placeMines()
        self.fillBoard()

        firstTurn = True
        isGameOver = False

        # run continuous game loop
        while (not isGameOver):
         
            self.displayBoard()
            
            # prompt the user to guess a tile
            input_col = int(input('Enter a Column: '))
            input_row = int(input('Enter a Row: '))

            # validate the input
            while (not (1 <= input_col <= self.num_cols and 1 <= input_row <= self.num_rows)):
                print('ERROR! INVALID INPUT!')
                input_col = int(input('Enter a Column: '))
                input_row = int(input('Enter a Row: '))
                
            input_col -= 1
            input_row -= 1

            # guarantee that the user guesses an empty space on the first guess
            if (firstTurn == True and not self.game_board[input_row][input_col].isEmpty()):
                # loop through the 8 adjacent tiles
                for r in range(input_row - 1, input_row + 2):
                    for c in range(input_col - 1, input_col + 2):
                        if (self.game_board[r][c].isMine()):
                            # move mine
                            self.game_board[r][c].value = ' ' 
                            # replace mine
                            self.placeMine()    

                self.fillBoard()

            # flip the tile the user guessed
            self.game_board[input_row][input_col].flip()

            # if the user guesses an empty tile...
            if (self.game_board[input_row][input_col].isEmpty()):
                self.clearEmptyCells(input_row, input_col)
            
            # if the users loses...
            if (self.hasLost(input_row, input_col)):
                self.lostGame()
                isGameOver = True

            # if the user wins...
            if (self.hasWon()):
                self.wonGame()
                isGameOver = True

            firstTurn = False
                
def main():

    game_board = GameBoard(9, 9, 10) # create a 9 x 9 game board with 10 mines
    game_board.gameLoop()

main()
