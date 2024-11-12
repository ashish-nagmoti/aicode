def is_safe(col_placement, row, col):
    # Check for conflicts in columns and diagonals
    for prev_row in range(row):
        prev_col = col_placement[prev_row]
        # Check same column or diagonals
        if prev_col == col or \
           abs(prev_col - col) == abs(prev_row - row):
            return False
    return True

def solve_n_queens(n, row, col_placement, results):
    if row == n:
        results.append(col_placement[:])
        return
    
    for col in range(n):
        if is_safe(col_placement, row, col):
            col_placement[row] = col  # Place queen in this column
            solve_n_queens(n, row + 1, col_placement, results)  # Move to next row
            col_placement[row] = -1  # Backtrack

def n_queens_branch_and_bound(n):
    results = []
    col_placement = [-1] * n  # Track column placements for each row
    solve_n_queens(n, 0, col_placement, results)  # Start solving from the first row
    return results

def print_solutions(solutions, n):
    for solution in solutions:
        print("Solution:")
        for row in solution:
            line = ['.'] * n
            line[row] = 'Q'
            print(" ".join(line))
        print("\n" + "-" * (2 * n - 1))  # Divider between solutions

# Example usage:
n = 8  # Number of queens
solutions = n_queens_branch_and_bound(n)

# Print each solution in Q and dot format
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions, n)
