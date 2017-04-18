import pygame
import gameboard
import button

# global variables
window_width = 400
window_height = 500

game_board_x = 25
game_board_y = 125
game_board_width = 350
game_board_height = 350

colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray1": (200, 200, 200),
    "gray2": (175, 175, 175),
    "blue1": (0, 0, 215),
    "blue2": (0, 0, 255),
    "blue3": (0, 0, 235),
    "red1": (215, 0, 0),
    "red2": (255, 0, 0),
    "red3": (235, 0, 0),
    "green1": (0, 135, 0),
    "green2": (0, 175, 0),
    "green3": (0, 155, 0)
}

buttons = {
    "start": button.Button(100, "Start"),
    "help": button.Button(175, "Help"),
    "settings": button.Button(250, "Settings"),
    "high_scores": button.Button(325, "High Scores"),
    "help_back": button.Button(400, "Back"),
    "settings_back": button.Button(400, "Back"),
    "high_scores_back": button.Button(400, "Back"),
    "easy": button.Button(100, "Easy"),
    "medium": button.Button(175, "Medium"),
    "hard": button.Button(250, "Hard"),
    "play-again": button.Button(250, "Play Again")
}

class GUI:

    # GUI constructor 
    def __init__(self):
        self.window = pygame.display.set_mode((window_width, window_height))

    # initialize pygame
    pygame.init()
    pygame.display.set_caption('Minesweeper')

    def text(self, txt, x, y, font, size, color, align):
        """
        - GUI display of text
        """
        f = pygame.font.SysFont(font, size)
        t = f.render(txt, True, color)

        if (align == "left"):
            self.window.blit(t, [x, y])
        elif (align == "center"):
            self.window.blit(t, [x - (t.get_rect().width / 2), y - (t.get_rect().height / 2)])

    def displayButton(self, button):
        """
        - GUI display of button from the Button class
        """     
        pygame.draw.rect(self.window, button.bgColor, [button.x, button.y, button.w, button.h])
        pygame.draw.rect(self.window, button.fgColor, [button.x + 5, button.y + 5, button.w - 10, button.h - 10])
        self.text(button.text, button.x + button.w / 2, button.y + button.h / 2, "Impact", 24, button.textColor, "center")

    def displayBoard(self, board, tile_width, tile_height, num_rows, num_cols):
        """
        - GUI display of the back end 2D array of the game board from the GameBoard class
        """
        w = tile_width
        h = tile_height

        for row in range(num_rows):
            for col in range(num_cols):
                x = col * w + game_board_x
                y = row * h + game_board_y
                
                if (board[row][col].isFlipped):
                    pygame.draw.rect(self.window, colors["gray1"], [x, y, w, h])
                    if (board[row][col].isMine()): 
                        self.text(board[row][col].value, x + (w / 2), y + h, "Impact", tile_width * 2, board[row][col].textColor(), "center")
                    else:
                        self.text(board[row][col].value, x + (w / 2), y + (h / 2), "Impact", tile_width, board[row][col].textColor(), "center")  
                else:
                    if (board[row][col].isFlagged):
                        pygame.draw.rect(self.window, colors["red1"], [x, y, w, h])
                        pygame.draw.rect(self.window, colors["red2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, colors["red3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
                    elif (board[row][col].isMarked):
                        pygame.draw.rect(self.window, colors["green1"], [x, y, w, h])
                        pygame.draw.rect(self.window, colors["green2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, colors["green3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
                    else:
                        pygame.draw.rect(self.window, colors["blue1"], [x, y, w, h])
                        pygame.draw.rect(self.window, colors["blue2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, colors["blue3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
             
    def gameLoop(self):
        """
        - menu system and game loop
        """
        screen = "main_menu_screen"
        openWindow = True
        difficulty = "easy"
        firstTurn = True

        while (openWindow):

            if (firstTurn):
                if (difficulty == "easy"):
                    num_rows = 9
                    num_cols = 9
                    num_mines = 10
                elif (difficulty == "medium"):
                    num_rows = 16
                    num_cols = 16
                    num_mines = 40
                elif (difficulty == "hard"):
                    num_rows = 18
                    num_cols = 18
                    num_mines = 64

                tile_width = game_board_width // num_cols
                tile_height = game_board_height // num_rows

                # create the game board
                game_board = gameboard.GameBoard(num_rows, num_cols, num_mines)

                # setup the game board
                game_board.createBoard()
                game_board.placeMines()
                game_board.fillBoard()

            # main menu screen
            if (screen == "main_menu_screen"):

                # update pygame frame
                pygame.display.update()

                # GUI display
                self.window.fill(colors["gray1"])
                self.text("Minesweeper", window_width / 2, 50, "Impact", 48, colors["white"], "center")  
                self.displayButton(buttons["start"])
                self.displayButton(buttons["help"])
                self.displayButton(buttons["settings"])
                self.displayButton(buttons["high_scores"])
                self.text("Created by Kevin Henneberger, Adam Wiener,", window_width / 2, 425, "Impact", 16, colors["white"], "center")  
                self.text("Matt Aber, and Baptiste Saliba", window_width / 2, 450, "Impact", 16, colors["white"], "center")

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # change screen
                        if (buttons["start"].mouseOver(mouseX, mouseY)):
                            screen = "play_game_screen"
                        elif (buttons["help"].mouseOver(mouseX, mouseY)):
                            screen = "help_screen"
                        elif (buttons["settings"].mouseOver(mouseX, mouseY)):
                            screen = "settings_screen"
                        elif (buttons["high_scores"].mouseOver(mouseX, mouseY)):
                            screen = "high_scores_screen"

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

            # help screen
            elif (screen == "help_screen"):

                # update pygame frame
                pygame.display.update()

                # GUI display
                self.window.fill(colors["gray1"])
                self.text("Help", window_width / 2, 50, "Impact", 48, colors["white"], "center")

                instructions = [
                    "Insert step 1 here...", 
                    "Insert step 2 here...", 
                    "Insert step 3 here...", 
                    "Insert step 4 here...", 
                    "Insert step 5 here..."
                ]

                for i in range(len(instructions)):
                    self.text(str(i + 1) + ") " + instructions[i], 35, i * 35 + 100, "Impact", 18, colors["white"], "left") 

                self.displayButton(buttons["help_back"])

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):

                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # change screen
                        if (buttons["help_back"].mouseOver(mouseX, mouseY)):
                            screen = "main_menu_screen"

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

            # settings screen
            elif (screen == "settings_screen"):

                # update pygame frame
                pygame.display.update()

                # GUI display
                self.window.fill(colors["gray1"])
                self.text("Settings", window_width / 2, 50, "Impact", 48, colors["white"], "center")
                self.displayButton(buttons["easy"])
                self.displayButton(buttons["medium"])
                self.displayButton(buttons["hard"])  
                self.displayButton(buttons["settings_back"])

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # change screen
                        if (buttons["easy"].mouseOver(mouseX, mouseY)):
                            difficulty = "easy"
                        elif (buttons["medium"].mouseOver(mouseX, mouseY)):
                            difficulty = "medium"
                        elif (buttons["hard"].mouseOver(mouseX, mouseY)):
                            difficulty = "hard"
                        elif (buttons["settings_back"].mouseOver(mouseX, mouseY)):
                            screen = "main_menu_screen"

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

                if (difficulty == "easy"): 
                    buttons["easy"].fgColor = (0, 200, 0)
                    buttons["medium"].fgColor = (200, 200, 200)
                    buttons["hard"].fgColor = (200, 200, 200)

                elif (difficulty == "medium"): 
                    buttons["medium"].fgColor = (0, 200, 0)
                    buttons["easy"].fgColor = (200, 200, 200)
                    buttons["hard"].fgColor = (200, 200, 200)
                else:
                    buttons["hard"].fgColor = (0, 200, 0)
                    buttons["easy"].fgColor = (200, 200, 200)
                    buttons["medium"].fgColor = (200, 200, 200)

            # high scores screen
            elif (screen == "high_scores_screen"):

                # update pygame frame
                pygame.display.update()

                # GUI display
                self.window.fill(colors["gray1"])
                self.text("High Scores", window_width / 2, 50, "Impact", 48, colors["white"], "center")  
                self.displayButton(buttons["high_scores_back"])

                high_scores_list = [
                    "Name 1 " + ". " * 40 + "100", 
                    "Name 2 " + ". " * 40 + "200",
                    "Name 3 " + ". " * 40 + "300", 
                    "Name 4 " + ". " * 40 + "400",
                    "Name 5 " + ". " * 40 + "500"
                ]

                for i in range(len(high_scores_list)):
                    self.text(str(i + 1) + ") " + high_scores_list[i], 35, i * 35 + 100, "Impact", 18, colors["white"], "left") 

                self.displayButton(buttons["help_back"])

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # change screen
                        if (buttons["high_scores_back"].mouseOver(mouseX, mouseY)):
                            screen = "main_menu_screen"

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

            # play game screen
            elif (screen == "play_game_screen"):

                # update pygame frame
                pygame.display.update()

                self.window.fill(colors["gray2"])

                # GUI display of board
                self.displayBoard(game_board.board, tile_width, tile_height, num_rows, num_cols)

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # convert mouseX and mouseY coordinates into row and column
                        input_col = int((mouseX - game_board_x) // tile_width)
                        input_row = int((mouseY - game_board_y) // tile_height)

                        # guarantee that the user guesses an empty space on the first guess
                        if (firstTurn):
                            game_board.guaranteeEmptyCell(input_row, input_col)

                        # if the user left clicks
                        if (event.button == 1 and not (game_board.board[input_row][input_col].isFlagged or game_board.board[input_row][input_col].isMarked)):
                            # flip the tile the user guessed
                            game_board.board[input_row][input_col].flip()

                            # if the user guesses an empty tile...
                            if (game_board.board[input_row][input_col].isEmpty()):
                                game_board.clearEmptyCells(input_row, input_col)

                            # if the users loses...
                            if (game_board.hasLost(input_row, input_col)):
                                screen = "lose_screen"

                            # if the user wins...
                            if (game_board.hasWon()):
                                screen = "win_screen"

                            firstTurn = False

                        # if the user right clicks
                        elif (event.button == 3 and firstTurn == False):

                            game_board.board[input_row][input_col].count += 1

                            # unmark the tile the user guessed as a flag
                            game_board.board[input_row][input_col].unflag()
                            # unmark the tile the user guessed as marked
                            game_board.board[input_row][input_col].unmark()
                        
                            if (game_board.board[input_row][input_col].count % 3 == 1):
                                # mark the tile the user guessed as a flag
                                game_board.board[input_row][input_col].flag()
                            elif (game_board.board[input_row][input_col].count % 3 == 2):
                                # mark the tile the user guessed as marked
                                game_board.board[input_row][input_col].mark()

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

            # lose screen
            elif (screen == "lose_screen"):

                # update pygame frame
                pygame.display.update()

                # GUI display
                game_board.revealMines()
                self.displayBoard(game_board.board, tile_width, tile_height, num_rows, num_cols)
                self.text("GAME OVER!", window_width / 2, 175, "Impact", 48, colors["white"], "center")  
                self.displayButton(buttons["play-again"])

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # change screen
                        if (buttons["play-again"].mouseOver(mouseX, mouseY)):
                            screen = "main_menu_screen"
                            firstTurn = True

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

            # win screen
            elif (screen == "win_screen"):

                # update pygame frame
                pygame.display.update()

                # GUI display
                self.displayBoard(game_board.board, tile_width, tile_height, num_rows, num_cols)
                font = pygame.font.SysFont("Impact", 48)
                self.text("YOU WIN!", window_width / 2, 175, "Impact", 48, colors["white"], "center")  
                self.displayButton(buttons["play-again"])

                # event handling
                for event in pygame.event.get():
                    # check if the user clicked the mouse
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        # get mouse x and y coordinates
                        mousePosition = pygame.mouse.get_pos()
                        mouseX = mousePosition[0]
                        mouseY = mousePosition[1]

                        # change screen
                        if (buttons["play-again"].mouseOver(mouseX, mouseY)):
                            screen = "main_menu_screen"
                            firstTurn = True

                    # allow the user to exit the window
                    if (event.type == pygame.QUIT):
                        openWindow = False

        pygame.quit()
        quit()
