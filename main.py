import pygame
import gameboard

pygame.init()

# global variables
num_rows = 18
num_cols = 18
num_mines = 10
screen_width = 400
screen_height = 400
tileW = screen_width // num_cols
tileH = screen_height // num_rows

# create a 9 x 9 game board with 10 mines
game_board = gameboard.GameBoard(num_rows, num_cols, num_mines)
# setup the game board
game_board.createBoard()
game_board.placeMines()
game_board.fillBoard()

# initialize pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Minesweeper')
screen.fill((200, 200, 200))

def displayBoard(board):
    """
    - GUI display of the back-end game board array from the GameBoard class
    """
    for row in range(num_rows):
        for col in range(num_cols):
            tileX = col * tileW
            tileY = row * tileH
            
            if (not board[row][col].isFlipped):
                pygame.draw.rect(screen, (0, 100, 255), [tileX, tileY, tileW, tileH])
                pygame.draw.rect(screen, (0, 75, 225), [tileX + (tileW // 18), tileY + (tileH // 18), tileW - (tileW // 9), tileH - (tileH // 9)])
            else: 
                pygame.draw.rect(screen, (200, 200, 200), [tileX, tileY, tileW, tileH])
                font = pygame.font.SysFont("monospace", 25)
                txt = font.render(board[row][col].value, True, (255, 255, 255))
                screen.blit(txt, [tileX - (txt.get_rect().width // 2) + (tileW // 2), tileY - (txt.get_rect().height // 2) + (tileH // 2)])

def gameLoop():
    """
    - game loop and menu system
    """
    openWindow = True   
    playGameScreen = True
    loseScreen = False
    winScreen = False

    firstTurn = True

    # open window loop
    while (openWindow):
        # event handling
        for event in pygame.event.get():
            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                openWindow = False

        # play game loop
        while (playGameScreen):

            # update pygame frame
            pygame.display.update()

            # GUI display of board
            displayBoard(game_board.board)

            # event handling
            for event in pygame.event.get():
                # allow the user to exit the window
                if (event.type == pygame.QUIT):
                    playGameScreen = False
                    openWindow = False

                # check if the user clicked the mouse
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    # get mouse x and y coordinates
                    mousePosition = pygame.mouse.get_pos()
                    mouseX = mousePosition[0]
                    mouseY = mousePosition[1]

                    # convert mouseX and mouseY into row and column
                    input_col = int(mouseX // tileW)
                    input_row = int(mouseY // tileH)

                    # guarantee that the user guesses an empty space on the first guess
                    if (firstTurn):
                        game_board.guaranteeEmptyCell(input_row, input_col)

                    # flip the tile the user guessed
                    game_board.board[input_row][input_col].flip()

                    # if the user guesses an empty tile...
                    if (game_board.board[input_row][input_col].isEmpty()):
                        game_board.clearEmptyCells(input_row, input_col)
                    
                    # if the users loses...
                    if (game_board.hasLost(input_row, input_col)):
                        playGameScreen = False
                        loseScreen = True

                    # if the user wins...
                    if (game_board.hasWon()):
                        playGameScreen = False
                        winScreen = True

                    firstTurn = False

        # lose screen loop
        while (loseScreen):

            # update pygame frame
            pygame.display.update()

            # GUI display of board
            game_board.revealMines()
            displayBoard(game_board.board)
            font = pygame.font.SysFont("monospace", 48)
            txt = font.render("GAME OVER!", True, (255, 0, 0))
            screen.blit(txt, [screen_width / 2 - (txt.get_rect().width // 2), screen_height / 4 - (txt.get_rect().height // 2)])    

            for event in pygame.event.get():
                # allow the user to exit the window
                if (event.type == pygame.QUIT):
                    openWindow = False
                    loseScreen = False

        # win screen loop
        while (winScreen):
            # update pygame frame
            pygame.display.update()

            # GUI display of board
            game_board.revealMines()
            displayBoard(game_board.board)
            font = pygame.font.SysFont("monospace", 48)
            txt = font.render("YOU WIN!", True, (0, 255, 0))
            screen.blit(txt, [screen_width / 2 - (txt.get_rect().width // 2), screen_height / 4 - (txt.get_rect().height // 2)])

            for event in pygame.event.get():
                # allow the user to exit the window
                if (event.type == pygame.QUIT):
                    openWindow = False
                    winScreen = False

    pygame.quit()
    quit()
                
def main():

    gameLoop()

main()
