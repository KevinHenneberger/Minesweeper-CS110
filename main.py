import gameboard

num_rows = 9
num_cols = 9
num_mines = 10

game_board = gameboard.GameBoard(num_rows, num_cols, num_mines) # create a 9 x 9 game board with 10 mines

def displayBoard(board):
    """
    - display the game board
    """
    for row in range(num_rows):
        print('|', end='')
        for col in range(num_cols):
            if (board[row][col].isFlipped):
                print(board[row][col].display(), end='|')
            else:
                print('#', end='|')
        print('')

def lostGame():
    """
    - lost game function
    """
    game_board.revealMines()
    displayBoard(game_board.board)
    print("GAME OVER!")

def wonGame():
    """
    - won game function
    """
    displayBoard(game_board.board)
    print('YOU WON!')

def gameLoop():
    """
    - run a continuous game loop that prompts the user to guess tiles until the game ends (user wins or loses)
    """
    # setup the game board
    game_board.createBoard()
    game_board.placeMines()
    game_board.fillBoard()

    firstTurn = True
    isGameOver = False

    # run continuous game loop
    while (not isGameOver):
     
        displayBoard(game_board.board)
        
        # prompt the user to guess a tile
        input_col = int(input('Enter a Column: '))
        input_row = int(input('Enter a Row: '))

        # validate the input
        while (not (1 <= input_col <= num_cols and 1 <= input_row <= num_rows)):
            print('ERROR! INVALID INPUT!')
            input_col = int(input('Enter a Column: '))
            input_row = int(input('Enter a Row: '))
            
        input_col -= 1
        input_row -= 1

        # guarantee that the user guesses an empty space on the first guess
        if (firstTurn == True):
            game_board.guaranteeEmptyCell(input_row, input_col)

        # flip the tile the user guessed
        game_board.board[input_row][input_col].flip()

        # if the user guesses an empty tile...
        if (game_board.board[input_row][input_col].isEmpty()):
            game_board.clearEmptyCells(input_row, input_col)
        
        # if the users loses...
        if (game_board.hasLost(input_row, input_col)):
            lostGame()
            isGameOver = True

        # if the user wins...
        if (game_board.hasWon()):
            wonGame()
            isGameOver = True

        firstTurn = False
                
def main():

    gameLoop()

main()
