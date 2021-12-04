balls = []
boards = []

for index, line in enumerate(open('input.txt').readlines()):
    if index == 0:  # first line is the numbers
        balls = [int(num) for num in line.split(',')]
        # Build a dictionary where the keys are the bingo numbers, and the values are the index when drawn
        ballsDict = dict(zip(balls, range(len(balls))))
    elif line == '\n':
        boards.append([])
    else:
        boards[-1].append([int(num) for num in line.split()])

lastBoard = -1
lastBoardMoves = 0
firstBoard = -1
firstBoardMoves = len(balls)

# Iterate each row and col on each board once and determine how many moves each row will take to be marked.
for boardIndex, board in enumerate(boards):
    winningRowMoves = len(balls)
    cols = [[row[index] for row in board] for index in range(len(board[0]))] # transpose the board to get the cols
    rowsAndCols = board + cols
    for row in rowsAndCols:
        moves = max([ballsDict[num] for num in row])
        # Determine how many moves it will take before there is a win on this board.
        if moves < winningRowMoves:
            winningRowMoves = moves

    # Determine which board will win first
    if winningRowMoves < firstBoardMoves:
        firstBoard = boardIndex
        firstBoardMoves = winningRowMoves

    # Determine which board will win last
    if winningRowMoves > lastBoardMoves:
        lastBoard = boardIndex
        lastBoardMoves = winningRowMoves 

def score(board, moves):
    nums = [num for row in board for num in row]
    sumOfUnmarkedNumbers = sum(num for num in nums if ballsDict[num] > moves)
    lastNumberCalled = balls[moves]
    return sumOfUnmarkedNumbers * lastNumberCalled

print('Part 1: (winning board score): ', score(boards[firstBoard], firstBoardMoves))
print('Part 2: (losing board score): ', score(boards[lastBoard], lastBoardMoves))