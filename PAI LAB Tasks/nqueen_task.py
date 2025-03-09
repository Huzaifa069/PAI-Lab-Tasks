def solve_n_queens(size):
    dp_table = [[0] * (1 << size) for _ in range(size + 1)]
    dp_table[0][0] = 1  # Initially, 1 way to have no queens placed
    
    # Iterate through each row
    for row in range(size):
        for column_mask in range(1 << size):  # Iterate through all possible column placements
            if dp_table[row][column_mask] == 0:
                continue  # Skip invalid states

            # Try placing a queen in each column
            for col in range(size):
                if column_mask & (1 << col) == 0:  # If column 'col' is free
                    new_mask = column_mask | (1 << col)  # Place queen at col
                    dp_table[row + 1][new_mask] += dp_table[row][column_mask]  # Update DP table

    return sum(dp_table[size])  # Sum of valid placements in last row


# Input from user
board_size = int(input("Enter N for N-Queen: "))
print("Total Solutions:", solve_n_queens(board_size))
