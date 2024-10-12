import random

def generate_sudoku_puzzle(size=9):
    """
    Generates a Sudoku puzzle of the specified size.

    Args:
        size (int): The size of the Sudoku puzzle (default is 9).

    Returns:
        list: A 2D list representing the Sudoku puzzle.
    """

    puzzle = [[0 for _ in range(size)] for _ in range(size)]
    fill_sudoku(puzzle)
    remove_cells(puzzle, 30)  # Remove 30 cells to create a solvable puzzle
    return puzzle

def fill_sudoku(puzzle):
    """
    Recursively fills the Sudoku puzzle with valid numbers.

    Args:
        puzzle (list): The Sudoku puzzle to fill.
    """

    size = len(puzzle)
    empty_cell = find_empty_cell(puzzle)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, size + 1):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            if fill_sudoku(puzzle):
                return True
            puzzle[row][col] = 0

    return False

def find_empty_cell(puzzle):
    """
    Finds an empty cell in the Sudoku puzzle.

    Args:
        puzzle (list): The Sudoku puzzle to search.

    Returns:
        tuple: A tuple containing the row and column indices of the empty cell, or None if no empty cells are found.
    """

    size = len(puzzle)
    for row in range(size):
        for col in range(size):
            if puzzle[row][col] == 0:
                return row, col
    return None

def is_valid(puzzle, row, col, num):
    """
    Checks if a number is valid for a given cell in the Sudoku puzzle.

    Args:
        puzzle (list): The Sudoku puzzle.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to check.

    Returns:
        bool: True if the number is valid, False otherwise.
    """

    size = len(puzzle)
    # Check row
    for i in range(size):
        if puzzle[row][i] == num:
            return False
    # Check column
    for i in range(size):
        if puzzle[i][col] == num:
            return False
    # Check 3x3 subgrid
    start_row = (row // (size // 3)) * (size // 3)
    start_col = (col // (size // 3)) * (size // 3)
    for i in range(start_row, start_row + (size // 3)):
        for j in range(start_col, start_col + (size // 3)):
            if puzzle[i][j] == num:
                return False
    return True

def remove_cells(puzzle, num_cells):
    """
    Removes a specified number of cells from the Sudoku puzzle to create a solvable puzzle.

    Args:
        puzzle (list): The Sudoku puzzle.
        num_cells (int): The number of cells to remove.
    """

    size = len(puzzle)
    while num_cells > 0:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            num_cells -= 1

def print_sudoku(puzzle):
    """
    Prints the Sudoku puzzle in a formatted way.

    Args:
        puzzle (list): The Sudoku puzzle to print.
    """

    size = len(puzzle)
    for i in range(size):
        if i % (size // 3) == 0 and i != 0:
            print("-" * (size * 3 + (size // 3) - 1))
        for j in range(size):
            if j % (size // 3) == 0 and j != 0:
                print("|", end=" ")
            print(puzzle[i][j], end=" ")
        print()

# Generate a Sudoku puzzle
puzzle = generate_sudoku_puzzle()

# Print the puzzle
print("Sudoku Puzzle:")
print_sudoku(puzzle)

# Get user input for missing numbers
missing_numbers = []
while True:
    row = int(input("Enter the row of a missing number (0 to quit): "))
    if row == 0:
        break
    col = int(input("Enter the column of the missing number: "))
    number = int(input("Enter the missing number: "))
    missing_numbers.append((row, col, number))

# Fill in the missing numbers
for row, col, number in missing_numbers:
    puzzle[row][col] = number

# Solve the puzzle
if fill_sudoku(puzzle):
    print("Solution:")
    print_sudoku(puzzle)
else:
    print("No solution found.")