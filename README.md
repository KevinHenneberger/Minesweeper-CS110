# Minesweeper

# Project Description
    - terminal version of Minesweeper in Python

# Key
    '#' = tile (not turned over)
    ' ' = empty tile
    '1' = tile that touches 1 mine, '2' = tile that touches 2 mines, '3' = tile that touches 3 mines, ...
    '*' = mine

# Classes

    class Tile
        Description
            - represents an individual tile in the game board

        Instance Variables 
            - row = row
            - col = column
            - value =  '#', ' ', '*', '1', '2', ...
            - isFlipped = boolean value for whether the user has flipped the title or not

        Methods
            - flip() = set isFlipped to True
            - isMine() = return if the tile is a mine or not
            - isEmpty = return if the tile is empty or not
            - display() = return the tile value

    class GameBoard
        Description:
            - represents the entire game board
            - store the game board as a 2D array of tile objects

        Instance Variables 
            - game_board = empty array that will be used to create and store the game board
            - num_rows = number of rows in the game board
            - num_cols = number of columns in the game board
            - num_mines = number mines in the game board

        Methods     
            - createBoard() = create a 2D array of tile objects (num_rows x num_cols)  
            - placeMine() = randomly place a mine in the game board
            - placeMines() = randomly place mines in the game board
            - fillBoard() = count the number of mines that touch each tile and assign the tile that value   
            - clearEmptyCells() = flip all of the adjacent empty tiles
            - revealMines() = reveal all of the mines
            - hasLost() = if the user guesses a mine, return True
            - hasWon() = if the user has flipped every tile that does not contain a mine, return True
            - lostGame() = lost game function
            - wonGame() = won game function
            - displayBoard() = print the properly formatted game board to the console
            - gameLoop() = run a continuous game loop that prompts the user to guess tiles until the game ends (user wins or loses)
