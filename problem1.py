"""
COMP4476 - Introduction to Cryptography
Francesco Coniglione (1206780)
Assignment 3 - Problem 1
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

def sum_column(grid, col_cell):
    # Sums the ith column of the grid and returns the result modulo 27
    return sum(row[col_cell] for row in grid) % 27

def shift_left(row, i):
    # Shifts the row to the left by i positions
    return row[i:] + row[:i]

def shift_down(grid, col_cell, i):
    # Shifts the column down by i positions
    col = [grid[row_cell][col_cell] for row_cell in range(5)]
    shifted_col = col[-i:] + col[:-i]
    for row_cell in range(5):
        grid[row_cell][col_cell] = shifted_col[row_cell]

def hash(text):
    # Must clean to ensure input fits the entire 5x5 grid and only contains valid characters
    cleaned = "".join([c.lower() for c in text if c.lower() in ALPHABET])
    while len(cleaned) % 25 != 0:
        cleaned += " "
    
    out = [0] * 5  # Initialized the output with all 0's

    # Process the cleaned text in blocks of 25 characters
    for b in range(0, len(cleaned), 25):
        block = cleaned[b:b+25]
        
        # Round 1
        grid = []
        for r in range(0, 25, 5):
            grid.append([ALPHABET.index(c) for c in block[r:r+5]])
        
        # Update output with Round 1 column sums
        for i in range(5):
            out[i] = (out[i] + sum_column(grid, i)) % 27

        # Round 2
        for i in range(5):
            grid[i] = shift_left(grid[i], i)
        
        # Update output with Round 2 column sums
        for i in range(5):
            out[i] = (out[i] + sum_column(grid, i)) % 27

        # Round 3
        for i in range(5):
            shift_down(grid, i, i)
        
        # Update output with Round 3 row sums
        for i in range(5):
            row_sum = sum(grid[i]) % 27
            out[i] = (out[i] + row_sum) % 27

    # Convert final output numbers back to characters
    final_hash = "".join([ALPHABET[n] for n in out])
    return final_hash, out

# Testing the hash function
plaintext = "the birthday attack can be performed for any hash functions including sha three"
result_str, result_nums = hash(plaintext)

print(f"Hash String: '{result_str}'")
print(f"Hash Values: {result_nums}")