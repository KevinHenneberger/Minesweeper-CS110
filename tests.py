import tile
import button
import gameboard

print("=" * 50)
print("### Testing the Tile Module (tile.py) ###")
print("=" * 50)

tile_test = tile.Tile(1, 1);
value = ['*', ' ', '1']

for v in value:

    tile_test.value = v
    
    print("Test isMine() and isEmpty() for the following value: ", v)
    print(tile_test.isMine())
    print(tile_test.isEmpty())
    
print("Flip Test #1 (should equal False)")
print(tile_test.isFlipped)
print("Flip Test #2 (should equal True)")
tile_test.flip()
print(tile_test.isFlipped)

print("Flag Test #1 (should equal False)")
print(tile_test.isFlagged)
print("Flag Test #2 (should equal True)")
tile_test.flag()
print(tile_test.isFlagged)
print("Flag Test #3 (should equal False)")
tile_test.unflag()
print(tile_test.isFlagged)
    
print("Mark Test #1 (should equal False)")
print(tile_test.isMarked)
print("Flag Test #2 (should equal True)")
tile_test.mark()
print(tile_test.isMarked)
print("Flag Test #3 (should equal False)")
tile_test.unmark()
print(tile_test.isMarked)

try:
    tile_test.textColor()
    print("Successful Color Test")
except:
    print("Failed Color Test")

print("=" * 50)
print("### Testing the Button Module (button.py) ###")
print("=" * 50)

button_test = button.Button(0, "Test")

print(button_test.mouseOver(121, 1)) # should equal True
print(button_test.mouseOver(1000, 1000)) # should equal False

print("=" * 50)
print("### Testing the GameBoard module (game board.py) ###")
print("=" * 50)

tests = [(10,10,9), (12,12,24), (16,16,40)] # the three difficulties: Easy, Medium, and Hard.

for t in tests:
    print("Attempt to create a board with {} rows, {} columns, and {} mines.".format(t[0], t[1], t[2]))
    gameboard_test = gameboard.GameBoard(t[0], t[1], t[2])
    gameboard_test.createBoard()
    gameboard_test.placeMine()
    gameboard_test.placeMines()
    gameboard_test.fillBoard()
    gameboard_test.clearEmptyCells(0, 1)
    gameboard_test.guaranteeEmptyCell(0, 1)
    gameboard_test.revealMines()
    gameboard_test.hasLost(0, 1)
    gameboard_test.hasWon()
    print("Successfully created board!")
