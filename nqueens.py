# O(n!) and O(n^2)
def is_safe(board, row, col):
   
    
    for i in range(col):
        if board[row][i] == 1:
            return False

    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    """Use backtracking to place queens on the board starting from the given column."""
    if col >= len(board):
        return True  

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  

            if solve_n_queens(board, col + 1):  
                return True

            board[i][col] = 0  

    return False  

def print_board(board):
    """Print the chessboard with queens."""
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print()

def solve_8_queens():
    """Function to solve the 8-Queens problem."""
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve_n_queens(board, 0):  
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    solve_8_queens()