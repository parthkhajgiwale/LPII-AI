def is_safe(board, row, col, n):
    """Check if placing a queen at board[row][col] is safe."""
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens_util(board, row, n):
    """Utility function to solve N Queens problem recursively."""
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = '_'

    return False


def solve_n_queens(n):
    """Solve N Queens problem."""
    board = [['_'] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return

    print("Solution:")
    for row in board:
        print(' '.join(row))


# Taking user input for board size (N)
n = int(input("Enter the number of queens (N): "))
solve_n_queens(n)
