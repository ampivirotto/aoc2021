
def convertCol(board):
    cols = {0:[], 1:[], 2:[], 3:[], 4:[]}

    for i in board:
        for k, j in enumerate(i):
            cols[k].append(j)
    return cols

def checkDiagonal(board):
    diags = {0:[], 1:[]}
    counter = 0 
    for i,k in enumerate(board):
        if i == counter:
            for j, m in enumerate(k):
                if j == counter:
                    diags[0].append(m)
                    counter += 1
                    break

    counterr = 0
    counterc = 4 
    for i,k in enumerate(board):
        if i == counterr:
            for j, m in enumerate(k):
                if j == counterc:
                    diags[1].append(m)
                    counterr += 1
                    counterc -= 1
    return diags

def checkboard(board):
    for row in board:
        if "".join(row) == 'XXXXX':
            return True
    cols = convertCol(board)
    for col in cols.values():
        if "".join(col) == 'XXXXX':
            return True
    diags = checkDiagonal(board)
    for diag in diags.values():
        if "".join(diag) == 'XXXXX':
            return True
    return False
    
def setupboards():
    counter = 0
    temp = []
    boards = {}
    c2 = 0

    with open("day4input.txt") as f:
        for line in f:
            if counter == 0:
                calls = line.split(",")

            elif counter > 0 and counter < 6:
                boardline = line.strip("\n").split(" ")
                removewhite = [i for i in boardline if i]
                temp.append(removewhite)

            if counter == 5:
                boards[c2] = temp
                c2 += 1
            counter += 1
            if line == "\n":
                counter = 1
                temp = []

    return calls, boards

def action(c, boards):
    for b in boards.values():
        for row in b:
            for index, item in enumerate(row):
                if item == c:
                    row[index] = 'X'
    return boards

def countUnmarked(board):
    total = 0
    for row in board:
        for item in row:
            if item == 'X':
                continue
            else:
                total += int(item)
    return total

def bestplay():
    calls, boards = setupboards()

    for call in calls:
        boards = action(call, boards)

        for board in boards.values():
            win = checkboard(board)
            if win == True:
                num = countUnmarked(board)
                return call, num

def worstplay():
    calls, boards = setupboards()

    for call in calls:
        boards = action(call, boards)

        copiedboards = dict(boards)
        for board in copiedboards.keys():
            win = checkboard(copiedboards[board])
            if win == True:
                if len(boards) > 1:
                    boards.pop(board)
                else:
                    return countUnmarked(boards[board]), int(call)
        

num, call = bestplay()
x = int(num) * int(call)
print(x)

num2, call2 = worstplay()
print(num2 * call2)