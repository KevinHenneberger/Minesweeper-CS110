import pygame
import gameboard
import button
import time
import highscores

class GameGUI:

    # GUI constructor 
    def __init__(self):
        self.window_w = 400
        self.window_h = 500
        self.window = pygame.display.set_mode((self.window_w, self.window_h))

        self.num_rows = 9
        self.num_cols = 9
        self.num_mines = 10
        self.game_board = gameboard.GameBoard(self.num_rows, self.num_cols, self.num_mines)

        self.game_board_x = 25
        self.game_board_y = 90
        self.game_board_w = 350
        self.game_board_h = 350

        self.tile_w = self.game_board_w // self.num_cols
        self.tile_h = self.game_board_h // self.num_rows

        self.screen = "main_menu_screen"
        self.difficulty = "easy"
        self.openWindow = True
        self.firstTurn = True
        self.start_time = time.time()
        self.mines_remaining = self.num_mines
        self.score = 0
        self.name = "player1"

        """
        dictionary of predefined colors
        """
        self.colors = {
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

        """
        dictionary of button objects from the Button class
        """
        self.buttons = {
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
            "start_back": button.Button(440, "Back"),
            "play-again-l": button.Button(200, "Play Again"),
            "play-again-w": button.Button(300, "Play Again")
        }

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
            self.window.blit(t, [x - (t.get_rect().w / 2), y - (t.get_rect().h / 2)])

    def displayButton(self, button):
        """
        - GUI display of button from the Button class
        """     
        pygame.draw.rect(self.window, button.bgColor, [button.x, button.y, button.w, button.h])
        pygame.draw.rect(self.window, button.fgColor, [button.x + 5, button.y + 5, button.w - 10, button.h - 10])
        self.text(button.text, button.x + button.w / 2, button.y + button.h / 2, "Impact", 24, button.textColor, "center")

    def displayBoard(self):
        """
        - GUI display of the back end 2D array of the game board from the GameBoard class
        """
        w = self.tile_w
        h = self.tile_h
        board = self.game_board.board

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = col * w + self.game_board_x
                y = row * h + self.game_board_y
                
                if (board[row][col].isFlipped):
                    pygame.draw.rect(self.window, self.colors["gray1"], [x, y, w, h])
                    if (board[row][col].isMine()): 
                        self.text(board[row][col].value, x + (w / 2), y + h, "Impact", w * 2, board[row][col].textColor(), "center")
                    else:
                        self.text(board[row][col].value, x + (w / 2), y + (h / 2), "Impact", w, board[row][col].textColor(), "center")  
                else:
                    if (board[row][col].isFlagged):
                        pygame.draw.rect(self.window, self.colors["red1"], [x, y, w, h])
                        pygame.draw.rect(self.window, self.colors["red2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, self.colors["red3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
                    elif (board[row][col].isMarked):
                        pygame.draw.rect(self.window, self.colors["green1"], [x, y, w, h])
                        pygame.draw.rect(self.window, self.colors["green2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, self.colors["green3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
                    else:
                        pygame.draw.rect(self.window, self.colors["blue1"], [x, y, w, h])
                        pygame.draw.rect(self.window, self.colors["blue2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, self.colors["blue3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
      
    def mainMenu(self):

        # update pygame frame
        pygame.display.update()

        # GUI display
        self.window.fill(self.colors["gray1"])
        self.text("Minesweeper", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")  
        self.displayButton(self.buttons["start"])
        self.displayButton(self.buttons["help"])
        self.displayButton(self.buttons["settings"])
        self.displayButton(self.buttons["high_scores"])
        self.text("Created by Kevin Henneberger, Adam Wiener,", self.window_w / 2, 425, "Impact", 16, self.colors["white"], "center")  
        self.text("Matt Aber, and Baptiste Saliba", self.window_w / 2, 450, "Impact", 16, self.colors["white"], "center")

        # event handling
        for event in pygame.event.get():
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["start"].mouseOver(mouseX, mouseY)):
                    self.screen = "play_game_screen"

                    # set up the board
                    self.firstTurn = True

                    if (self.difficulty == "easy"):
                        self.num_rows = 9
                        self.num_cols = 9
                        self.num_mines = 10
                        self.mines_remaining = 10
                    elif (self.difficulty == "medium"):
                        self.num_rows = 12
                        self.num_cols = 12
                        self.num_mines = 24
                        self.mines_remaining = 24
                    elif (self.difficulty == "hard"):
                        self.num_rows = 16
                        self.num_cols = 16
                        self.num_mines = 40
                        self.mines_remaining = 40

                    self.game_board = gameboard.GameBoard(self.num_rows, self.num_cols, self.num_mines)
                    self.game_board.createBoard()
                    self.game_board.placeMines()
                    self.game_board.fillBoard()
                    self.tile_w = self.game_board_w // self.num_cols
                    self.tile_h = self.game_board_h // self.num_rows

                    self.start_time = time.time()

                elif (self.buttons["help"].mouseOver(mouseX, mouseY)):
                    self.screen = "help_screen"
                elif (self.buttons["settings"].mouseOver(mouseX, mouseY)):
                    self.screen = "settings_screen"
                elif (self.buttons["high_scores"].mouseOver(mouseX, mouseY)):
                    self.screen = "high_scores_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                self.openWindow = False

    def playGameScreen(self):

        # update pygame frame
        pygame.display.update()

        current_time = time.time()
        self.score = int(current_time - self.start_time)

        minutes, seconds = divmod(self.score, 60)
        formatted_score = ("%2d:%02d" % (minutes, seconds))

        self.window.fill(self.colors["gray2"])
        pygame.draw.rect(self.window, self.colors["gray1"], [25, 25, 100, 50])
        self.text(str(self.mines_remaining), 75, 48, "Impact", 50, self.colors["red1"], "center")
        pygame.draw.rect(self.window, self.colors["gray1"], [265, 25, 100, 50])
        self.text(str(formatted_score), 310, 48, "Impact", 50, self.colors["red1"], "center")
        self.displayButton(self.buttons["start_back"])

        # GUI display of board
        self.displayBoard()

        # event handling
        for event in pygame.event.get():
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["start_back"].mouseOver(mouseX, mouseY)):
                    self.screen = "main_menu_screen"

                # convert mouseX and mouseY coordinates into row and column
                input_col = int((mouseX - self.game_board_x) // self.tile_w)
                input_row = int((mouseY - self.game_board_y) // self.tile_h)

                # prevent index errors
                if (0 <= input_col < self.num_cols and 0 <= input_row < self.num_cols):

                    # guarantee that the user guesses an empty space on the first guess
                    if (self.firstTurn):
                        self.game_board.guaranteeEmptyCell(input_row, input_col)

                    # if the user left clicks
                    if (event.button == 1 and not (self.game_board.board[input_row][input_col].isFlagged or self.game_board.board[input_row][input_col].isMarked)):
                        # flip the tile the user guessed
                        self.game_board.board[input_row][input_col].flip()

                        # if the user guesses an empty tile...
                        if (self.game_board.board[input_row][input_col].isEmpty()):
                            self.game_board.clearEmptyCells(input_row, input_col)

                        # if the users loses...
                        if (self.game_board.hasLost(input_row, input_col)):
                            self.screen = "lose_screen"

                        # if the user wins...
                        if (self.game_board.hasWon()):
                            self.screen = "win_screen"

                        self.firstTurn = False

                    # if the user right clicks
                    elif (event.button == 3 and self.firstTurn == False):

                        self.game_board.board[input_row][input_col].count += 1

                        # unmark the tile the user guessed as a flag
                        self.game_board.board[input_row][input_col].unflag()
                        # unmark the tile the user guessed as marked
                        self.game_board.board[input_row][input_col].unmark()
                    
                        if (self.game_board.board[input_row][input_col].count % 3 == 1):
                            # mark the tile the user guessed as a flag
                            self.game_board.board[input_row][input_col].flag()
                            self.mines_remaining -= 1
                        elif (self.game_board.board[input_row][input_col].count % 3 == 2):
                            # mark the tile the user guessed as marked
                            self.game_board.board[input_row][input_col].mark()
                            self.mines_remaining += 1

            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                self.openWindow = False

    def helpScreen(self):

        # update pygame frame
        pygame.display.update()

        # GUI display
        self.window.fill(self.colors["gray1"])
        self.text("Help", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")

        instructions = [
            "* To win, open all the cells which do not contain a mine.",
            "* Try to win as quickly as possible.",
            "* If you guess a cell with a mine, you lose.",
            "* Every non-mine cell will tell you the total number of mines",
            "  in the eight neighboring cells.",
            "* To open a square, point at the square and click on it.",
            "* To mark a square you think is a mine with a flag, point",
            "  and right-click.",
            "* Right-click twice to mark a cell that you are unsure about.",
            "* The first square you open is never a mine.",
            "* The upper left corner contains the number of mines left to find.",
            "* The upper right corner contains a time counter.",
            "* Good luck sweeping!"
        ]

        for i in range(len(instructions)):
            self.text(instructions[i], 15, i * 20 + 85, "Impact", 14, self.colors["white"], "left") 

        self.displayButton(self.buttons["help_back"])

        # event handling
        for event in pygame.event.get():
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):

                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["help_back"].mouseOver(mouseX, mouseY)):
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                self.openWindow = False

    def settingsScreen(self):

        # update pygame frame
        pygame.display.update()

        # GUI display
        self.window.fill(self.colors["gray1"])
        self.text("Settings", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")
        self.displayButton(self.buttons["easy"])
        self.displayButton(self.buttons["medium"])
        self.displayButton(self.buttons["hard"])  
        self.displayButton(self.buttons["settings_back"])

        # event handling
        for event in pygame.event.get():
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["easy"].mouseOver(mouseX, mouseY)):
                    self.difficulty = "easy"
                elif (self.buttons["medium"].mouseOver(mouseX, mouseY)):
                    self.difficulty = "medium"
                elif (self.buttons["hard"].mouseOver(mouseX, mouseY)):
                    self.difficulty = "hard"
                elif (self.buttons["settings_back"].mouseOver(mouseX, mouseY)):
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                self.openWindow = False

        if (self.difficulty == "easy"): 
            self.buttons["easy"].fgColor = (0, 200, 0)
            self.buttons["medium"].fgColor = (200, 200, 200)
            self.buttons["hard"].fgColor = (200, 200, 200)

        elif (self.difficulty == "medium"): 
            self.buttons["medium"].fgColor = (0, 200, 0)
            self.buttons["easy"].fgColor = (200, 200, 200)
            self.buttons["hard"].fgColor = (200, 200, 200)
        else:
            self.buttons["hard"].fgColor = (0, 200, 0)
            self.buttons["easy"].fgColor = (200, 200, 200)
            self.buttons["medium"].fgColor = (200, 200, 200)

    def highScoreScreen(self):

        # update pygame frame
        pygame.display.update()

        # GUI display
        self.window.fill(self.colors["gray1"])
        self.text("High Scores", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")  
        self.displayButton(self.buttons["high_scores_back"])

        hs = highscores.HighScores().outputData()

        for i in range(len(hs)):
            name, score = hs[i]
            self.text(str(i + 1) + ") " + name, 100, i * 28 + 100, "Impact", 18, self.colors["white"], "left") 
            self.text(str(score), 265, i * 28 + 100, "Impact", 18, self.colors["white"], "left") 

        self.displayButton(self.buttons["help_back"]) 

        # event handling
        for event in pygame.event.get():
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["high_scores_back"].mouseOver(mouseX, mouseY)):
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                self.openWindow = False

    def loseScreen(self):

        # update pygame frame
        pygame.display.update()

        # GUI display
        self.window.fill(self.colors["gray1"])
        self.game_board.revealMines()
        self.displayBoard()
        self.text("Game Over!", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")  
        self.displayButton(self.buttons["play-again-l"])

        # event handling
        for event in pygame.event.get():
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["play-again-l"].mouseOver(mouseX, mouseY)):
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):
                self.openWindow = False

    def winScreen(self):

        # update pygame frame
        pygame.display.update()

        # GUI display
        self.window.fill(self.colors["gray1"])
        self.displayBoard()
        font = pygame.font.SysFont("Impact", 48)
        self.text("You Win!", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")  
        self.displayButton(self.buttons["play-again-w"])

        pygame.draw.rect(self.window, self.colors["gray2"], [20, 115, 360, 50])
        self.text("Score: " + str(self.score), 25, 125, "Impact", 25, self.colors["white"], "left")  

        pygame.draw.rect(self.window, self.colors["gray2"], [20, 190, 360, 50])
        self.text("Enter a name: " + self.name, 25, 200, "Impact", 25, self.colors["white"], "left")

        # event handling
        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN):
                if (event.key == 8):
                    self.name = self.name[:-1]
                else:
                    self.name += chr(event.key)

            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()
                mouseX = mousePosition[0]
                mouseY = mousePosition[1]

                # change screen
                if (self.buttons["play-again-w"].mouseOver(mouseX, mouseY)):
                    # add score to JSON file
                    highscores.HighScores().addData(self.name, self.score)
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            elif (event.type == pygame.QUIT):
                self.openWindow = False

    def gameLoop(self):
        """
        - menu system and game loop
        """
        while (self.openWindow):

            # main menu screen
            if (self.screen == "main_menu_screen"):
                self.mainMenu()
            # help screen
            elif (self.screen == "help_screen"):
                self.helpScreen()
            # settings screen
            elif (self.screen == "settings_screen"):
                self.settingsScreen()
            # high scores screen
            elif (self.screen == "high_scores_screen"):
                self.highScoreScreen()
            # play game screen
            elif (self.screen == "play_game_screen"):
                self.playGameScreen()
            # lose screen
            elif (self.screen == "lose_screen"):
                self.loseScreen()
            # win screen
            elif (self.screen == "win_screen"):
                self.winScreen()

        # quit pygame
        pygame.quit()
        quit()
