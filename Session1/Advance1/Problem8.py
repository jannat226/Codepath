# Problem 8: Local Maximums
# Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

# local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

def local_maximums(grid):
    n = len(grid)
    local_maxes = []
    for i in range(len(grid)-2):
        row=[]
        for j in range(len(grid)-2):
            max_val = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    max_val = max(max_val, grid[x][y])
            row.append(max_val)
        local_maxes.append(row)

    print(local_maxes)
# 4x4 matrix with cells numbered according to Example 1 input next to 2x2 matrix numbered according Example 1 output

# Example Usage:

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
local_maximums(grid)

# grid = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 2, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1]
# ]
# local_maximums(grid)
# Example Output:

# [[9, 9], [8, 6]]
# [[2, 2, 2], [2, 2, 2], [2, 2, 2]]