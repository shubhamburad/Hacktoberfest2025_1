# Python program to solve the N-Queens Problem

def printSolution(board):
    for row in board:
        print(row)
    print()

def isSafe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solveNQueens(board, row, n):
    if row == n:
        printSolution(board)
        return

    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            solveNQueens(board, row + 1, n)
            board[row][col] = 0  # backtrack

def nQueens(n):
    board = [[0] * n for _ in range(n)]
    solveNQueens(board, 0, n)

# Run for 4 queens
nQueens(4)
