import tile
import gameboard

print("######## Testing Tile Model #########")
test_tile = tile.Tile(1, 1);

# print True
test_tile.value = '*'
print(test_tile.isMine())

# print False
test_tile.value = '1'
print(test_tile.isMine())

# print True
test_tile.value = ' '
print(test_tile.isEmpty())

# print False
test_tile.value = '1'
print(test_tile.isEmpty())

# print False
print(test_tile.isFlipped)
test_tile.flip()
# print True
print(test_tile.isFlipped)

print("######## Testing GameBoard Model #########")

tests = [(9, 9, 9), (1, 1, 1), (15, 15, 9), (9, 9, 0)]

for test in tests:
    test_gameboard1 = gameboard.GameBoard(test[0], test[1], test[2])
    test_gameboard1.createBoard()
    test_gameboard1.placeMines()
    test_gameboard1.fillBoard()
