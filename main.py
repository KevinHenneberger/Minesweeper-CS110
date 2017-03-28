import gameboard

game_board = gameboard.GameBoard(9, 9, 10) # create a 9 x 9 game board with 10 mines
                
def main():
    
    game_board.gameLoop()

main()
