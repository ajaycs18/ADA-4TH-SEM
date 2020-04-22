n = int(input('enter n: ')) 
board = [[0] * n for _ in range(n)]

def printBoard(board, n):
    for i in range(n):
        for ele in board[i]:
            print(ele, end=' ') 
        print()
    print()

def safe(board, i, j):
    # Check same row 
    if 1 in board[i]:
        return False

    # Check left upper diagonal
    i1, j1 = i - 1, j - 1
    while i1 > -1 and j1 > -1: 
        if board[i1][j1] == 1:
           return False
        i1 -= 1
        j1 -= 1 

    # Check left lower diagonal
    n = len(board)
    i2, j2 = i + 1, j - 1
    while i2 < n and j2 < n:
        if board[i2][j2] == 1:
            return False
        i2 += 1
        j2 -= 1

    return True


def nQueens(n, board, col=0):
    if col == n:
        printBoard(board, n)
        return

    for row in range(n):
        if safe(board, row, col):
            board[row][col] = 1
            nQueens(n, board, col + 1)
        board[row][col] = 0

nQueens(n, board)
