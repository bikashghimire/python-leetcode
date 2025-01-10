"""
Description:
You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to return the number of negative numbers present in the matrix."""
def countNegatives(grid):
    # Implement your solution here
    add = 0
    for i in grid:
        for j in i:
            if j < 0:
                add += 1
    return add
                
