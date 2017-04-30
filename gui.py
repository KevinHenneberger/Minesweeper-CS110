import pygame       #This module, not native to Python, but not written by us, is used for displaying the game.
import gameboard    #This module, written by us, constructs the game.
import button       #This module, written by us, constructs the buttons that are displayed in Pygame. The buttons allow the player to interact with the computer via the graphical user interface displayed by Pygame.
import time         #This module, native to Python, is used herein for measuring the time that the player takes in finishing the game.

class GameGUI:      #This class describes the graphical user interface of the game of Minesweeper. It particularly describes how the gameboard is to be displayed. The design of the gameboard is already prespecified in the module gameboard.py. This class uses Pygame for the display of the graphical user interface.

    # GUI constructor 
    def __init__(self):        #This method constructs the graphical user interface (the GUI).
        self.window_w = 400    #The width of the window.
        self.window_h = 500    #The height of the window.
        self.window = pygame.display.set_mode((self.window_w, self.window_h))    #This displays the window, given the prespecified dimensions of the window.

        self.num_rows = 9    #The gameboard is initialized so that it has nine rows.
        self.num_cols = 9    #The gameboard is initialized so that it has nine columns.
        self.num_mines = 0  #The gameboard is initialized so that it has zero mines.
        self.game_board = gameboard.GameBoard(self.num_rows, self.num_cols, self.num_mines)    #The gameboard is set up with the initialized states. These states persist for as long as the difficulty of the game is not changed. This means that, without having changed the difficulty, the player always wins as soon as he selects a tile.

        self.game_board_x = 25     #The x-coordinate of the gameboard's location.
        self.game_board_y = 125    #The y-coordinate of the gameboard's location.
        self.game_board_w = 350    #The width of the gameboard. The gameboard is a square.
        self.game_board_h = 350    #The height of the gameboard. The gameboard is a square.

        self.tile_w = self.game_board_w // self.num_cols    #The width of a single tile. The tile is a square. Its width equals the width of the board divided evenly by the number of columns. That is, the width of a tile equals the width of a row divided by the number of tiles per row.
        self.tile_h = self.game_board_h // self.num_rows    #The height of a single tile. The tile is a square. Its height equals the height of the board divided evenly by the number of rows. That is, the height of a tile equals the height of a column divided by the number of tiles per column.

        self.screen = "main_menu_screen"    #This sets Main Menu screen as the default screen. This screen will be the hub for all parts of the game, including the Play Game, Help, Settings, and High Scores screens. The Main Menu screen is not yet constructed.
        self.difficulty = "easy"            #The game's difficulty is set to Easy by default.
        self.openWindow = True              #The window is open.
        self.firstTurn = True               #By default, the player is on his first turn in the game. He has not yet selected his first tile. This is relevant for guaranteeEmptyCells() in gameboard.py.
        self.start_time = time.time()       #The amount of time that the player takes to complete the game will be measured. The measuring, from zero seconds, starts here.
        self.mines_remaining = self.num_mines    #This initializes the number of mines left to be found, so that it equals the total number of mines in the game. No mine has been flagged yet.
        self.score = 0    #The score of the player is by default set to 0.
        self.name = "player1"    #The name of the player is by default set to player1.

        self.high_scores_list = []    #A list containing the high scores of past games is created.

        """
        dictionary of predefined colors
        """
        self.colors = {                                  #This is a dictionary of every color in the game, except for the colors used for the numbers of flipped empty tiles.
            "white": (255, 255, 255),                    #This is the color of all text that is not part of the gameboard.
            "black": (0, 0, 0),
            "gray1": (200, 200, 200),                    #The next two colors are used for everything that is not assigned to another color in this dictionary. These two colors are particularly used for the backgrounds of the screens and the buttons. The lighter grey is preferred as a foreground color, whereas the darker grey is preferred as a background color.
            "gray2": (175, 175, 175),
            "blue1": (0, 0, 215),                        #The next three colors are for the sprite of an unflagged, unmarked tile, the default state. This tile is presented by default, or can be obtained by right clicking a marked tile. This sprite comprises an interior blue square with two outer square borders, each farther border having a darker hue than the parts within it.
            "blue2": (0, 0, 255),
            "blue3": (0, 0, 235),
            "red1": (215, 0, 0),                         #The next three colors are for the sprite of a so-called flagged tile. A flagged tile is a tile that has been flagged by the player (by right clicking a default tile) for having a mine underneath it. This sprite comprises an interior red square with two outer square borders, each farther border having a darker hue than the parts within it.
            "red2": (255, 0, 0),
            "red3": (235, 0, 0),
            "green1": (0, 135, 0),                       #The next three colors are for the sprite of a so-called marked tile. A marked tile is a tile that has been marked by the player (by right clicking a flagged tile) for having a state not yet determined by him. This sprite comprises an interior green square with two outer square borders, each farther border having a darker hue than the parts within it.
            "green2": (0, 175, 0),
            "green3": (0, 155, 0)
        }

        """
        dictionary of button objects from the Button class
        """
        self.buttons = {                                             #This is a dictionary of every button in the game. The values are the buttons. The keys denote the purposes of the buttons. For each value, the first argument is the y-coordinate of the button. The second argument is the text that appears on the button.
            "start": button.Button(100, "Start"),                    #The first four buttons take the player to from the main menu to different screens.
            "help": button.Button(175, "Help"),
            "settings": button.Button(250, "Settings"),
            "high_scores": button.Button(325, "High Scores"),
            "help_back": button.Button(400, "Back"),                 #The next three buttons take the player back to the main menu screen from a different screen. These other screens are the Help, Settings, and High Scores screens.
            "settings_back": button.Button(400, "Back"),
            "high_scores_back": button.Button(400, "Back"),
            "easy": button.Button(100, "Easy"),                      #The next three buttons are used for selecting a level of difficulty of the game. They are all on the Settings screen.
            "medium": button.Button(175, "Medium"),
            "hard": button.Button(250, "Hard"),
            "play-again-l": button.Button(200, "Play Again"),        #The next two buttons are used for returning to the main menu from the Play Game Screen. They are displayed after the game has been finished. The first of these two buttons is displayed only when the player loses the game. It differs from the second button by its vertical location on the screen.
            "play-again-w": button.Button(300, "Play Again")         #The second of these two buttons is displayed only when the player wins the game. It differs from the first button by its vertical location on the screen.
        }

    # initialize pygame
    pygame.init()    #Pygame is initialized.
    pygame.display.set_caption('Minesweeper')    #This sets the text displayed in the window, not in the screen. It is displayed in the top left corner.

    def text(self, txt, x, y, font, size, color, align):    #This method designs text to be used in the game.
        """
        - GUI display of text
        """
        f = pygame.font.SysFont(font, size)    #This sets the typeface and font size of the text.
        t = f.render(txt, True, color)         #This sets the text to be displayed, and sets its color.

        if (align == "left"):                  #This block of code sets the location of the text.
            self.window.blit(t, [x, y])
        elif (align == "center"):
            self.window.blit(t, [x - (t.get_rect().w / 2), y - (t.get_rect().h / 2)])

    def displayButton(self, button):    #This method designs the generic form of the button that is used throughout this game. The different buttons are differentiated by their locations and texts.
        """
        - GUI display of button from the Button class
        """     
        pygame.draw.rect(self.window, button.bgColor, [button.x, button.y, button.w, button.h])    #Create the interior of the button, using its location in x- and y-coordinates, and its width and height, and its color.
        pygame.draw.rect(self.window, button.fgColor, [button.x + 5, button.y + 5, button.w - 10, button.h - 10])    #Analogously, create the outer border of the button. This border is going to be in a darker color than the interior of the button.
        self.text(button.text, button.x + button.w / 2, button.y + button.h / 2, "Impact", 24, button.textColor, "center")    #Place the text inside the button using the text() method. The text will go at the specified location within the button, it will have the specified color, it will be centered within the button, and it will be presented in the Impact typeface, with a font size of 24.

    def displayBoard(self, board, tile_w, tile_h, num_rows, num_cols):    #This method designs the way that the tiles of the gameboard look.
        """
        - GUI display of the back end 2D array of the game board from the GameBoard class
        """
        w = tile_w    #The width of the tile.
        h = tile_h    #The height of the tile.

        for row in range(num_rows):        #These two for loops look at every tile on the gameboard.
            for col in range(num_cols):
                x = col * w + self.game_board_x    #This sets the x-coordinate of the gameboard. This is separate from determing where the player has to click in order to select a tile.
                y = row * h + self.game_board_y     #This sets the y-coordinate of the gameboard. This is separate from determining where the player has to click in order to select a tile.
                
                if (board[row][col].isFlipped):
                    pygame.draw.rect(self.window, self.colors["gray1"], [x, y, w, h])
                    if (board[row][col].isMine()): 
                        self.text(board[row][col].value, x + (w / 2), y + h, "Impact", tile_w * 2, board[row][col].textColor(), "center")   #If the flipped tile is a mine, then center a red asterisk character twice the width of the tile, and of the Impact typeface, within the tile.
                    else:
                        self.text(board[row][col].value, x + (w / 2), y + (h / 2), "Impact", tile_w, board[row][col].textColor(), "center") #If the flipped tile is a not a mine, then center the character corresponding to its value, its width equalling the width of the tile, and of the Impact typeface, within the tile.
                else:
                    if (board[row][col].isFlagged):              #This if block creates the sprite of a flagged tile, putting the three differently colored parts at the specified coordinates.
                        pygame.draw.rect(self.window, self.colors["red1"], [x, y, w, h])
                        pygame.draw.rect(self.window, self.colors["red2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, self.colors["red3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
                    elif (board[row][col].isMarked):             #This if block creates the sprite of a marked tile, putting the three differently colored parts at the specified coordinates.
                        pygame.draw.rect(self.window, self.colors["green1"], [x, y, w, h])
                        pygame.draw.rect(self.window, self.colors["green2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, self.colors["green3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
                    else:                                        #This if block creates the sprite of a default tile, putting the three differently colored parts at the specified coordinates.
                        pygame.draw.rect(self.window, self.colors["blue1"], [x, y, w, h])
                        pygame.draw.rect(self.window, self.colors["blue2"], [x + (w / 20), y + (h / 20), w - (w / 10), h - (h / 10)])
                        pygame.draw.rect(self.window, self.colors["blue3"], [x + (w / 4), y + (h / 4), w - (w / 2), h - (h / 2)])
      
    def mainMenu(self):    #This method designs the Main Menu screen, which is the default screen when the program is executed.

        # update pygame frame
        pygame.display.update()    #This updates the Pygame frame.

        # GUI display
        self.window.fill(self.colors["gray1"])        #This sets up the window of the Main Menu screen, and fills it with the color light grey.
        self.text("Minesweeper", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")    #This places the title of the game (Minesweeper) at the top of the screen, with the appropriate typeface (Impact), font size (48), color (white), and alignment (center).
        self.displayButton(self.buttons["start"])        #The next four lines display the four buttons on the Main Menu screen: Play Game, Help, Settings, and High Scores. The buttons lead to those screens.
        self.displayButton(self.buttons["help"])
        self.displayButton(self.buttons["settings"])
        self.displayButton(self.buttons["high_scores"])
        self.text("Created by Kevin Henneberger, Adam Wiener,", self.window_w / 2, 425, "Impact", 16, self.colors["white"], "center")    #Similarly to the title of the game, these next two lines of code display the creators of the program.
        self.text("Matt Aber, and Baptiste Saliba", self.window_w / 2, 450, "Impact", 16, self.colors["white"], "center")

        # event handling
        for event in pygame.event.get():    #This for loop looks through the events received by Pygame.
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):    #A restriction: out of all the events received, look at the presses of the mouse buttons.
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()    #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]    #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]    #The y-coordinate of the location at which the mouse was pressed.

                # change screen
                if (self.buttons["start"].mouseOver(mouseX, mouseY)):    #If the coordinates of the press of the mouse are inside of the geometric area of the Play Game button, then go to the Play Game screen.
                    self.screen = "play_game_screen"
                    self.start_time = time.time()                        #As soon as the player enters the Start screen, start the timer, to time how long the player takes to finish the game.
                elif (self.buttons["help"].mouseOver(mouseX, mouseY)):   #If the coordinates of the press of the mouse are inside of the geometric area of the Help button, then go to the Help screen.
                    self.screen = "help_screen"
                elif (self.buttons["settings"].mouseOver(mouseX, mouseY)):      #If the coordinates of the press of the mouse are inside of the geometric area of the Settings button, then go to the Settings screen.
                    self.screen = "settings_screen"
                elif (self.buttons["high_scores"].mouseOver(mouseX, mouseY)):   #If the coordinates of the press of the mouse are inside of the geometric area of the High Scores button, then go to the High Scores screen.
                    self.screen = "high_scores_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):        #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False            #If this event has been received, then close the program's open window.

    def playGameScreen(self):    #This method designs the Play Game screen, which is the screen in which the game is played.

        # update pygame frame
        pygame.display.update()    #This updates the Pygame frame.

        current_time = time.time()    #This determines the current time.
        self.score = int(current_time - self.start_time)    #The player's score is the amount of time that has elapsed.

        self.window.fill(self.colors["gray2"])    #This fills the screen with the color dark grey.
        pygame.draw.rect(self.window, self.colors["gray1"], [60, 25, 80, 50])                   #A light grey rectangle is displayed as a background for the text display of the number of mines in the game. It is located at the coordinates (60, 25), and has width 80 and height 50.
        self.text(str(self.num_mines), 100, 48, "Impact", 50, self.colors["red1"], "center")    #The number of mines in the game is displayed at the coordinates (100, 48) in the Impact typeface, in font size 50, in the color dark red, aligned with the center.
        pygame.draw.rect(self.window, self.colors["gray1"], [260, 25, 80, 50])                  #A light grey rectangle is displayed as a background for the player's score. It is located at the coordinates (260, 25), and has width 80 and height 50.
        self.text(str(self.score), 300, 48, "Impact", 50, self.colors["red1"], "center")        #The player's score is displayed at the coordinates (300, 48) in the Impact typeface, in font size 50, in the color dark red, aligned with the center.

        # GUI display of board
        self.displayBoard(self.game_board.board, self.tile_w, self.tile_h, self.num_rows, self.num_cols)        #This displays the board in the Play Game screen.

        # event handling
        for event in pygame.event.get():                        #This for loop looks through the events received by Pygame.
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):          #A restriction: out of all the events received, look at the presses of the mouse buttons.
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()          #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]                       #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]                       #The y-coordinate of the location at which the mouse was pressed.

                # convert mouseX and mouseY coordinates into row and column
                input_col = int((mouseX - self.game_board_x) // self.tile_w)    #Determine in which column the mouse was pressed, based on the x-coordinate of the press of the mouse.
                input_row = int((mouseY - self.game_board_y) // self.tile_h)    #Determine in which row the mouse was pressed, based on the y-coordinate of the press of the mouse.

                # prevent index errors
                if (0 <= input_col < self.num_cols and 0 <= input_row < self.num_cols):        #A further restriction: execute the following code only if the player has pressed on as location that is within the gameboard (i.e. on a row and column that exist in the gameboard).

                    # guarantee that the user guesses an empty space on the first guess
                    if (self.firstTurn):                                                       #A further restriction: if this is the player's first selection of a tile, then ensure, using guaranteeEmptycell() from gameboard.py, that the first tile selected is an empty cell. This prevents the user from unfairly losing on his first try, without having been given any useful information on where in the gameboard the mines are. The method guaranteeEmptyCells() moves any mine under the first tile selected to a different empty tile, and then the values of the empty cells (the numbers of mines to which each empty cell is adjacent) are refreshed.
                        self.game_board.guaranteeEmptyCell(input_row, input_col)

                    # if the user left clicks
                    if (event.button == 1 and not (self.game_board.board[input_row][input_col].isFlagged or self.game_board.board[input_row][input_col].isMarked)):    #A further restriction: of all the mouse presses, look at the presses that were both of the left mouse button, and on an unflipped default tile.
                        # flip the tile the user guessed
                        self.game_board.board[input_row][input_col].flip()             #Flip the tile.

                        # if the user guesses an empty tile...
                        if (self.game_board.board[input_row][input_col].isEmpty()):    #If the player has selected an empty tile, then flip that tile and all contiguous empty tiles.
                            self.game_board.clearEmptyCells(input_row, input_col)

                        # if the user loses...
                        if (self.game_board.hasLost(input_row, input_col)):            #If the player has selected a mine, then end the game and send the user to the Loss screen.
                            self.screen = "lose_screen"

                        # if the user wins...
                        if (self.game_board.hasWon()):                                 #If the player has flipped every empty tile, then the player has won, so send the player to the Win screen.
                            self.screen = "win_screen"

                        self.firstTurn = False                                         #All of this code is in a for loop, so that the code runs for every one of the player's turns. However, after this point in the first execution of the code, the player's first turn has ended, so change this flag to False. Otherwise, selection of a tile would be impossible even on the first turn.

                    # if the user right clicks
                    elif (event.button == 3 and self.firstTurn == False):              #A further restriction: of all the mouse presses, look at the presses that were both of the right mouse button, and performed after the player's first turn.

                        self.game_board.board[input_row][input_col].count += 1         #This counts the number of times that the right mouse button has been pressed. The variable count equals this number.

                        # unmark the tile the user guessed as a flag
                        self.game_board.board[input_row][input_col].unflag()           #Unflag a tile.
                        # unmark the tile the user guessed as marked
                        self.game_board.board[input_row][input_col].unmark()           #Unmark a tile.
                    
                        if (self.game_board.board[input_row][input_col].count % 3 == 1):      #count modulo 3 equals the number of right clicks past the default tile that the player has performed. One right click past the default tile makes for a flagged tile.
                            # mark the tile the user guessed as a flag
                            self.game_board.board[input_row][input_col].flag()                #Flag the selected tile.
                            self.num_mines -= 1                                               #Flagging a tile means that the tile has been identified as having a mine underneath it. Therefore, when one tile is flagged, decrease the number of tiles remaining to be found by 1. This number can go below 0 if too many tiles are flagged. If the number goes below 0, then the player knows that he has flagged too many tiles.
                        elif (self.game_board.board[input_row][input_col].count % 3 == 2):    #count modulo 3 equals the number of right clicks past the default tile that the player has performed. Two right clicks past the default tile makes for a marked tile.
                            # mark the tile the user guessed as marked
                            self.game_board.board[input_row][input_col].mark()                #Mark the selected tile. A tile must be flagged in order for the player to be able to mark it.
                            self.num_mines += 1                                               #Increase the number of tiles remaining to be found by 1. This undoes the flagging's effect of decreasing the number of tiles remaining to be found by 1. Marking only means that the player does not know what is beneath the tile.

            # allow the user to exit the window
            if (event.type == pygame.QUIT):        #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False            #If this event has been received, then close the program's open window.

    def helpScreen(self):    #This method designs the Help screen, which displays instructions for the player, for playing the game.

        # update pygame frame
        pygame.display.update()    #This updates the Pygame frame.

        # GUI display
        self.window.fill(self.colors["gray1"])        #This fills the screen with the color light grey.
        self.text("Help", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")    #This places the title of the screen (Help) at the specified location, with the appropriate typeface (Impact), font size (48), color (white), and alignment (center).

        instructions = [                                                               #This is the text (intended as a set of instructions to the player) that is displayed on the Help screen. Each line is displayed on its own line.
            "* To win, open all the cells that do not contain a mine.",
            "* Try to win as quickly as possible.",
            "* If you select a cell with a mine, you lose the game.",
            "* Every non-mine cell, when flipped, will tell you the total number of mines",
            "  in the eight neighboring cells.",
            "* To select a tile, point at the tile and click on it.",
            "* To mark a tile that you think is a mine, point",
            "  and right-click. This colors the tile red.",
            "* Marking the mines is not necessary for winning the game.",
            "* Right-click on a red tile to mark a tile that you are unsure about.",
            "  This makes the tile green. To set the tile back to blue, right-click it."
            "* The first tile you select is never a mine.",
            "* The upper left corner contains the number of mines unmarked in the game.",
            "* The upper right corner contains a time counter.",
            "* Good luck sweeping!"
        ]

        for i in range(len(instructions)):
            self.text(instructions[i], 15, i * 20 + 85, "Impact", 14, self.colors["white"], "left")    #This places the instructions at the location specified, with the appropriate typeface (Impact), font size (14), color (white), and alignment (left).

        self.displayButton(self.buttons["help_back"])     #This displays the button leading back to the Main Menu screen.

        # event handling
        for event in pygame.event.get():                  #This for loop looks through the events received by Pygame.
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):    #A restriction: out of all the events received, look at the presses of the mouse buttons.

                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()    #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]                 #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]                 #The y-coordinate of the location at which the mouse was pressed.

                # change screen
                if (self.buttons["help_back"].mouseOver(mouseX, mouseY)):    #If the coordinates of the press of the mouse are inside of the geometric area of the Back button, then go to the Main Menu screen.
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):               #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False                   #If this event has been received, then close the program's open window.

    def settingsScreen(self):    #This method designs the Settings screen, which displays the difficulty settings of the game.

        # update pygame frame
        pygame.display.update()    #Update the Pygame frame.

        # GUI display
        self.window.fill(self.colors["gray1"])                    #This fills the screen with the color of light grey.
        self.text("Settings", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")    #This places the title of the screen (Settings) at the top of the screen, with the appropriate typeface (Impact), font size (48), color (white), and alignment (center).
        self.displayButton(self.buttons["easy"])                  #This displays the Easy button, for the Easy difficulty.
        self.displayButton(self.buttons["medium"])                #This displays the Medium button, for the Medium, difficulty.
        self.displayButton(self.buttons["hard"])                  #This displays the Hard button, for the Hard difficulty.
        self.displayButton(self.buttons["settings_back"])         #This displays the Back button of the Settings screen, for returning to the Main Menu screen.

        # event handling
        for event in pygame.event.get():                          #This for loop looks through the events received by Pygame.
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):            #A restriction: out of all the events received, look at the presses of the mouse buttons.
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()            #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]                         #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]                         #The y-coordinate of the location at which the mouse was pressed.

                # change screen
                if (self.buttons["easy"].mouseOver(mouseX, mouseY)):                #If the coordinates of the press of the mouse are inside of the geometric area of the Easy button, then set the states of the game so that they are the Easy states.
                    self.difficulty = "easy"
                    self.num_rows = 9                                               #The next four lines set the Easy states. There are 9 rows, 9 columns, 10 mines, and 10 mines remaining to be found (this number decreases if some mines are flagged).
                    self.num_cols = 9
                    self.num_mines = 10
                    self.mines_remaining = 10
                elif (self.buttons["medium"].mouseOver(mouseX, mouseY)):            #If the coordinates of the press of the mouse are inside of the geometric area of the Medium button, then set the states of the game so that they are the Medium states.
                    self.difficulty = "medium"
                    self.num_rows = 12                                              #The next four lines set the Medium states. There are 12 rows, 12 columns, 24 mines, and 24 mines remaining to be found (this number decreases if some mines are flagged).
                    self.num_cols = 12
                    self.num_mines = 24
                    self.mines_remaining = 24
                elif (self.buttons["hard"].mouseOver(mouseX, mouseY)):              #If the coordinates of the press of the mouse are inside of the geometric area of the Hard button, then set the states of the game so that they are the Hard states.
                    self.difficulty = "hard"
                    self.num_rows = 16                                              #The next four lines set the Hard states. There are 16 rows, 16 columns, 40 mines, and 40 mines remaining to be found (this number decreases if some mines are flagged).
                    self.num_cols = 16
                    self.num_mines = 40
                    self.mines_remaining = 40
                elif (self.buttons["settings_back"].mouseOver(mouseX, mouseY)):     #If the coordinates of the press of the mouse are inside of the geometric area of the Back button, then go back to the Main Menu screen.
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):    #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False        #If this event has been received, then close the program's open window.

        if (self.difficulty == "easy"):                          #If the difficulty is Easy, then set the interior of the Easy button to the color green, and set the interiors of the Medium and Hard buttons to the color light grey.
            self.buttons["easy"].fgColor = (0, 200, 0)
            self.buttons["medium"].fgColor = (200, 200, 200)
            self.buttons["hard"].fgColor = (200, 200, 200)

        elif (self.difficulty == "medium"):                      #If the difficulty is Medium, then set the interior of the Medium button to the color green, and set the interiors of the Easy and Hard buttons to the color light grey.
            self.buttons["medium"].fgColor = (0, 200, 0)
            self.buttons["easy"].fgColor = (200, 200, 200)
            self.buttons["hard"].fgColor = (200, 200, 200)
        else:
            self.buttons["hard"].fgColor = (0, 200, 0)           #If the difficulty is Hard, then set the interior of the Hard button to the color green, and set the interiors of the Easy and Medium buttons to the color light grey.
            self.buttons["easy"].fgColor = (200, 200, 200)
            self.buttons["medium"].fgColor = (200, 200, 200)

    def highScoreScreen(self):    #This method designs the High Scores screen, which displays the high scores of players of the game.

        # update pygame frame
        pygame.display.update()    #Update the Pygame frame.

        # GUI display
        self.window.fill(self.colors["gray1"])                  #This fills the screen with the color light grey.
        self.text("High Scores", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")    #This places the title of the screen (High Scores) at the top of the screen, with the appropriate typeface (Impact), font size (48), color (white), and alignment (center).
        self.displayButton(self.buttons["high_scores_back"])    #This displays the Back button of the High Scores screen, which sends the player to the Main Menu screen.

        for i in range(len(self.high_scores_list)):             #This places the text of the players' high scores at the specified location, with the appropriate typeface (Impact), font size (18), color (white), and alignment (left). The text of each high score includes the score, preceded by "[number of entry]) [player's name] - ".
            self.text(str(i + 1) + ") " + self.high_scores_list[i][0] + " - " + self.high_scores_list[i][1], 35, i * 35 + 100, "Impact", 18, self.colors["white"], "left") 

        self.displayButton(self.buttons["help_back"])           #This displays the Back button of the Help screen, which sends the player to the Main Menu screen.

        # event handling
        for event in pygame.event.get():                        #This for loop looks through the events received by Pygame.
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):          #A restriction: out of all the events received, look at the presses of the mouse buttons.
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()          #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]                       #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]                       #The y-coordinate of the location at which the mouse was pressed.

                # change screen
                if (self.buttons["high_scores_back"].mouseOver(mouseX, mouseY)):    #If the coordinates of the press of the mouse are inside of the geometric area of the Back button, then go back to the Main Menu screen.
                    self.screen = "main_menu_screen"

            # allow the user to exit the window
            if (event.type == pygame.QUIT):    #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False        #If this event has been received, then close the program's open window.

    def loseScreen(self):    #This method designs the Loss screen, which is displayed when the player loses the game.

        # update pygame frame
        pygame.display.update()    #Update the Pygame frame.

        # GUI display
        self.window.fill(self.colors["gray1"])                #This fills the screen with the color light grey.
        self.game_board.revealMines()                         #This method, from, gameboard.py, flips every mine tile when the game has been lost, showing the red asterisks in place of the default blue square tiles.
        self.displayBoard(self.game_board.board, self.tile_w, self.tile_h, self.num_rows, self.num_cols)    #This displays the board exactly as it was when the player finished with it, and also with the mine tiles flipped. If this line were not here, then the entire board would no longer be displayed on the Loss screen.
        self.text("Game Over!", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")        #This places text, indicating that the game has been lost, at the top of the screen, with the appropriate typeface (Impact), font size (48), color (white), and alignment (center).
        self.displayButton(self.buttons["play-again-l"])      #This displays the Back button of the Loss screen, which sends the player to the Main Menu screen. It is differentiated from the Back button of the Win screen by its location.

        # event handling
        for event in pygame.event.get():                      #This for loop looks through the events received by Pygame.
            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):        #A restriction: out of all the events received, look at the presses of the mouse buttons.
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()        #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]                     #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]                     #The y-coordinate of the location at which the mouse was pressed.

                # change screen
                if (self.buttons["play-again-l"].mouseOver(mouseX, mouseY)):    #If the coordinates of the press of the mouse are inside of the geometric area of the Back button, then go back to the Main Menu screen.
                    self.screen = "main_menu_screen"
                    self.firstTurn = True      #Reset the firstTurn flag to true so that the computer understands that, the next time the player tries to play the game, it will be the player's first turn. Then, the computer will execute guaranteeEmptyCells() in gameboard.py.

            # allow the user to exit the window
            if (event.type == pygame.QUIT):    #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False        #If this event has been received, then close the program's open window.

    def winScreen(self):    #This method designs the Loss screen, which is displayed when the player loses the game.

        # update pygame frame
        pygame.display.update()    #Update the Pygame frame.

        # GUI display
        self.window.fill(self.colors["gray1"])                #This fills the screen with the color light grey.
        self.displayBoard(self.game_board.board, self.tile_w, self.tile_h, self.num_rows, self.num_cols)    #This displays the board exactly as it was when the player finished with it. If this line were not here, then the entire board would no longer be displayed on the Win screen.
        font = pygame.font.SysFont("Impact", 48)              #This sets the typeface to Impact, and the font size to 48.
        self.text("You Win!", self.window_w / 2, 50, "Impact", 48, self.colors["white"], "center")          #This places text, indicating that the game has been won, at the top of the screen, with the appropriate typeface (Impact), font size (48), color (white), and alignment (center).
        self.displayButton(self.buttons["play-again-w"])      #This displays the Back button of the Win screen, which sends the player to the Main Menu screen. It is differentiated from the Back button of the Loss screen by its location.

        pygame.draw.rect(self.window, self.colors["gray2"], [20, 115, 360, 50])    #A dark grey rectangle is displayed as a background for the player's final score. It is located at the coordinates (20, 115), and has width 360 and height 50.
        self.text("Score: " + str(self.score), 25, 125, "Impact", 25, self.colors["white"], "left")     #The player's final score is displayed at the coordinates (25, 125) in the Impact typeface, in font size 25, in the color white, aligned with the left.

        pygame.draw.rect(self.window, self.colors["gray2"], [20, 190, 360, 50])    #A dark grey rectangle is displayed as a background for the player's name (which is input by the player). It is located at the coordinates (20, 190), and has width 360 and height 50. The text for the player's final score comprises the numerical value of the player's final score, preceded by the text "Score: ".
        self.text("Enter a name: " + self.name, 25, 200, "Impact", 25, self.colors["white"], "left")    #The player's name (which is input by the player) is displayed at the coordinates (25, 200) in the Impact typeface, in font size 25, in the color white, aligned with the left. The text for the player's name comprises the player's name (previously input by the user), preceded by the text "Enter a name: ". By default, the player's name is player1, and this is displayed here in the game by default.

        # event handling
        for event in pygame.event.get():    #This for loop looks through the events received by Pygame.

            if (event.type == pygame.KEYDOWN):    #A restriction: out of all the events received, look at the presses of the keyboard buttons (the keys).
                if (event.key == 8):              #A restriction. The ASCII character with the number 8 is the Backspace character. This condition stipulates that if the player presses the Backspace key, the input player's name should be replaced by the same string except for its final character. Without this condition, it would be impossible for the player to delete an input character.
                    self.name = self.name[:-1]
                else:                             #This covers all cases in which the previous condition is not met. That is, this else statement covers all key presses that are not of the Backspace key. If any key other than the Backspace key is pressed, add its character to the end of the string of characters input by the player here in the game.
                    self.name += chr(event.key)

            # check if the user clicked the mouse
            if (event.type == pygame.MOUSEBUTTONDOWN):    #A restriction: out of all the events received, look at the presses of the mouse buttons.
                # get mouse x and y coordinates
                mousePosition = pygame.mouse.get_pos()    #Get a list of the two coordinates at which the mouse was pressed.
                mouseX = mousePosition[0]                 #The x-coordinate of the location at which the mouse was pressed.
                mouseY = mousePosition[1]                 #The y-coordinate of the location at which the mouse was pressed.

                # change screen
                if (self.buttons["play-again-w"].mouseOver(mouseX, mouseY)):      #If the coordinates of the press of the mouse are inside of the geometric area of the Back button, then go back to the Main Menu screen.
                    self.high_scores_list.append((self.name, str(self.score)))    #Add the player's high score, from this instance of the player winning the game, to the list of players' high scores.
                    self.screen = "main_menu_screen"
                    self.firstTurn = True                 #Reset the firstTurn flag to true so that the computer understands that, the next time the player tries to play the game, it will be the player's first turn. Then, the computer will execute guaranteeEmptyCells() in gameboard.py.

            # allow the user to exit the window
            elif (event.type == pygame.QUIT):    #A restriction: out of all the events received, look also at requests for Pygame to quit its execution.
                self.openWindow = False          #If this event has been received, then close the program's open window.

    def gameLoop(self):    #This method calls all the different functions from gameboard.py and gui.py that are required in order to set up the game. After this method has been executed, the game is completely set up and ready to be played.
        """
        - menu system and game loop
        """
        while (self.openWindow):    #While the window for the game is open.

            if (self.firstTurn):    #When it is the player's first turn (i.e. before the player has started playing)create the gameboard with the prespecified numbers of rows, column, and mines. Place the mines in the board (under the mine tiles), and give to the empty tiles values denoting the numbers of adjacent mines.
                self.game_board = gameboard.GameBoard(self.num_rows, self.num_cols, self.num_mines)    #Initialize the states of the gameboard, those states being the number of rows, the number of columns, and the number of mines. Construct the Gameboard object, known as the gameboard.
                self.game_board.createBoard()                       #According to the previously specified number of rows to be used in the gameboard, add that number of empty elements to the previously initialized gameboard. Each element represents a row, so that the board is filled with rows. Into each row, add a column of empty tiles. Each tile is indexed by its row and column indices. This completes the array that is the gameboard, and fills the gameboard with empty tiles.
                self.game_board.placeMines()                        #Do the following for the total number of mines (already specified) that must be present in the gameboard. Determine randomly the row index of the mine, corresponding to the row index of a tile. Determine randomly the column index of the mine, corresponding to the column index of a tile. Ensure that no two mines have the same row and column indices. If the mine of interest is set as having indices already taken by another mine, reassign for the mine of interest these indices randomly. Set the value of the mine tile to that of a mine, analogously to how the value of an empty cell is set.
                self.game_board.fillBoard()                         #To every empty tile in the gameboard, assign the value corresponding to the number of mines adjacent to it.
                self.tile_w = self.game_board_w // self.num_cols    #The width of a single tile. The tile is a square. Its width equals the width of the board divided evenly by the number of columns. That is, the width of a tile equals the width of a row divided by the number of tiles per row.
                self.tile_h = self.game_board_h // self.num_rows    #The height of a single tile. The tile is a square. Its height equals the height of the board divided evenly by the number of rows. That is, the height of a tile equals the height of a column divided by the number of tiles per column.

            # main menu screen
            if (self.screen == "main_menu_screen"):        #If the player is supposed to be on the Main Menu screen, then construct the Main Menu screen.
                self.mainMenu()

            # help screen
            elif (self.screen == "help_screen"):           #If the player is supposed to be on the Help screen, then construct the Help screen.
                self.helpScreen()

            # settings screen
            elif (self.screen == "settings_screen"):       #If the player is supposed to be on the Settings screen, then construct the Settings screen.
                self.settingsScreen()

            # high scores screen
            elif (self.screen == "high_scores_screen"):    #If the player is supposed to be on the High Scores screen, then construct the High Scores screen.
                self.highScoreScreen()

            # play game screen
            elif (self.screen == "play_game_screen"):      #If the player is supposed to be on the Play Game screen, then construct the Play Game screen.        
                self.playGameScreen()

            # lose screen
            elif (self.screen == "lose_screen"):           #If the player is supposed to be on the Loss screen, then construct the Loss screen.
                self.loseScreen()

            # win screen
            elif (self.screen == "win_screen"):            #If the player is supposed to be on the Win screen, then construct the Win screen.
                self.winScreen()

        pygame.quit()    #Uninitialize all Pygame modules that have been initialized. This does not end the program.
        quit()           #Quit the program.

