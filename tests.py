import tile
import gameboard

print("=" * 50)
print("### Testing Tile Model ###")
print("=" * 50)

tile_test = tile.Tile(1, 1);
value = ['*', ' ', '1']

for v in value:

    tile_test.value = v

    print("Test .isMine() and .isEmpty() for " + v)
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

print("=" * 50)
print("### Testing GameBoard Model ###")
print("=" * 50)

tests = [(5,5,3), (4,4,4), (9,9,9), (7,7,15)]

for t in tests:
    print("Attempt to create a board with {} rows, {} columns, and {} mines.".format(t[0], t[1], t[2]))
    testboard1 = gameboard.GameBoard(t[0], t[1], t[2])
    testboard1.createBoard()
    testboard1.placeMines()
    testboard1.fillBoard()
    print("Successfully created board!")
