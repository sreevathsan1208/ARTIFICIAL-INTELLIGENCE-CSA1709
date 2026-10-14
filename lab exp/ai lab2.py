N = 8

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()

def is_safe(board, row, col):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col):
    # Base case: All queens are placed
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1 # Place queen

            if solve_nq_util(board, col + 1):
                return True
            
            # Backtrack
            board[i][col] = 0 

    return False

def solve_nq():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nq_util(board, 0):
        print("Solution does not exist")
        return False

    print("One valid 8-Queen configuration (1 represents a Queen):")
    print_solution(board)
    return True

solve_nq()
