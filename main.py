#Programming Concepts and Applications with Python (LEC) - 10375 - CS 110 - A 0
#Matthew Aber, Kenneth Henneberger, Baptiste Saliba, and Adam Wiener
#Due: Thursday 4 May 2017
#Professor Steven Allen Moore
#Final Project


#This program runs the game Minesweeper. It is written by the authors named above.


import gui     #This module, written by us, is imported here so that the function main() can execute the method gameLoop() from the module gui.py. 

def main():    #This function executes the method that sets up the game of Minesweeper.
    gui.GameGUI().gameLoop()    #After this method has been executed, the game is completely set up and ready to be played.

main()         #The main() function is executed. gameLoop() in gui.py is executed, setting up the game of Minesweeper.
