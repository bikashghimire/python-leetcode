"""
Maximum difference between two consecutive elements in a list.
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements."""
def max_consecutive_difference(lst):
    if len(lst) < 2:  # If there are fewer than 2 elements, return 0
        return 0

    max_diff = []  # Initialize maximum difference
    for i in range(len(lst) - 1):
        # Compute the absolute difference between consecutive elements
        diff = abs(lst[i + 1] - lst[i])
        # Update max_diff if the current difference is greater
        max_diff.append(diff)

    return max(max_diff)


