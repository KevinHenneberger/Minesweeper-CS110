print("Hello World!") #31/70    #problems solved/problems

"""

This is a list of problems, concerns, and notes. This list is exhaustive, and its entries are in the order in which I noticed them as I documented the code. This list includes nothing about the module highscores.py. The problems are differentiated by having "* " in front of them. Some of the problems and concerns are already fixed, and I am working on the ones that are not fixed, except for the high scores problems, which I don't understand.
I am going to go through every single thing in this list and fix it, if someone else has not fixed it.

People should be able to choose the number of mines. Put it in a button.
* [FIXED] * Fix the timer's display format
* [FIXED] * Fix the score display.
mines with timers???
Timer counting down?
* documentation
* [FIXED] * add quit button so that IDLE does not close when Close (on the window) is pressed. <--- I forgot what this means. Basically add a Quit button to the Main Menu screen.
* make it so the game doesn't not work as soon as it is opened
add the number of non-mine tiles remaining to be flipped
* [FIXED] * add a back button on the game play screen
placeMine() in gameboard.py can be condensed into a single while loop.
placeMine() and placeMines() in gameboard.py can be condensed into a single method.
rename placeMine() or placeMines() to differentiate the names more.
Why does placeMine() say self.board[mine_row][mine_col].value = '*' instead of using the isMine method in the Tile class?
why does fillBoard() in gameboard.py not make use of the methods in the Tile class to set the text in the empty tiles?
[FIXED] Change the name of num_mines_touches in fillBoard() in gameboard.py.
Is the final else statement in fillBoard() in gameboard.py unnecessary? Aren't the empty tiles preset to the value ' '? Play Again doesn't work if the else statement is removed. Why?
[FIXED] What is clearEmptyCells() in gameboard.py saying?
Should the mines be flipped when the player wins the game?
[FIXED] In guaranteeEmptyCell() in gameboard.py, can a mine be placed back at its original location?
[FIXED] In guaranteeEmptyCell() in gameboard.py, after placeMine() is executed, are the values of the empty cells updated? Yes.
Why are there for loops in guaranteeEmptyCell() in gameboard.py? Can't they be eliminated?
* [FIXED] * Change the text on the Play Again button when the game ends.
Should the placement of the buttons, shown when the game has been won, be changed? They obscure the gameboard.
* Fix the display of the high scores. Currently, they just display in the order that the games were played.
* Typing the player's name into the box when the game is won is difficult.
* Also, the Shift and Caps Lock keys, and presumably others, do not do what they are supposed to do.
* Also, the high scores input is probably prompted regardless of the player's score.
* Also, the high scores run off the bottom of the screen.
* Why does __init__() in gui.py initialize the board to (9, 9, 0)?
[FIXED] Rename the play_again_l and play_again_w buttons so that their names are clearer.
[FIXED] Why do the two play_again buttons do the same thing? Can one be eliminated?
* [FIXED] * Rename the play_again buttons main_menu, and add a single play_again button that restarts the game without forcing the player to go to the main menu.
[FIXED] Rename the back buttons as main_menu buttons?
[FIXED] Change the names of the colors to make them clearer. Change 1, 2, and 3, to dark, light, and medium, respectively. Change gray to grey.
[FIXED] Black is not used anywhere in the game, and should be removed from the color dictionary in __init__() in gui.py.
* [FIXED] * Update the Help or Settings screens to tell the player how many mines are in each level of difficulty. Easy has 10. Medium has 24. Hard has 40. Also tell the sizes of the boards.
What is the purpose of True in t = f.render(txt, True, color) in text() in gui.py?
[FIXED] What does the alignment part of text() in gui.py mean?
In gui.py, what sets the gameboard's location?
[FIXED] In gui.py, what are tile_w and tile_h?
* In gui.py, in mainMenu(), what is the event type pygame.QUIT? How does the player perform this event?
* [FIXED] * Change Start to Play Game.
[FIXED] Rename mines_remaining in __init__() in gui.py.
Should playGameScreen() in gui.py, in its if statement on left clicks, include a condition that the tile be unflipped?
[FIXED] Change Lose screen to Loss screen.
In gui.py, in playGameScreen(), move self.firstTurn = False into the if statement that asks whether this turn is the player's first turn.
Currently, marking or flagging a tile is explicitly impossible on the first turn. The code does not have to be written like that.
* Marking is BROKEN!!!!! As you mark tiles, the displayed number of mines decreases. If you finish the game and restart the game without having changed the difficulty, the decreased number of mines is displayed, and this is the actual number of mines in the game.
For some reasons, the method guaranteeEmptyCells() usually places the mine either on the edge of the gameboard, or one block in from the edge of the gameboard.
fillBoard() in gameboard.py fills only the empty cells. The mines are filled in placeMine().
* [FIXED] * In gui.py, tile_w and tile_h are defined twice. Once in __init__(), and once in gameLoop(). I deleted the first definitions.
* In the previous note why did deleting the first two definitions not seem to change anything about the game?
* [FIXED] * In gui.py, in gameLoop(), what do pygame.quit() and quit() do? If both are removed, the program does not close. If only quit() is removed, the program closes effortlessly. If only pygame.quit() is removed, trying to close the program requires special permission to kill the program, because the program is still running. Removing neither has the same effect.
[FIXED] What does count do?
In gui.py, is mousePosition = pygame.mouse.get_pos() a list or a tuple?
[FIXED] Two different back buttons are constructed in highScoreScreen(), in gui.py, even though only one is shown: the High Scores back button and the Help back button.
[FIXED] Also, change the name of highScoreScreen() to highScoresScreen() in gui.py.
[FIXED] Finish the documentation for playGameScreen in gui.py.
In settingsScreen() in gui.py, should the settings of the colors of the selected difficulty buttons to green come before the pygame.QUIT lines?
What is game_board in self.game_board.revealMines() in loseScreen() in gui.py? It does not work if it is changed to gameboard. This method executes revealMines() from gameboard.py.
In winScreen(), in gui.py, what is the purpose of font = pygame.font.SysFont("Impact", 48)? Eliminating this line does not seem to change the game.
[FIXED] In winScreen(), in gui.py, finish the documentation for the keyboard presses.
* Is it a problem that at least one class (gui.py) contains executable code? Should the executable code be moved to main.py?
* Add documentation to main.py explaining what this program does.
Can all the different for loops in gui.py be made as only one for loop that does not have to be entirely rewritten every time it is used?
[FIXED] Why does the timer have to start in mainMenu()?
[FIXED] Right-clicking on any button is the same as left-clicking it.
[FIXED] Tiles that have already been flipped can be flipped, flagged, and marked.
Add black borders to the buttons of the Loss Screen and Win Screen, so that the buttons stand out against the background (the gameboard).

"""
