"""
Description:

Given an array arr of length n, consisting of integers, find the sum of the subarray (including an empty subarray) that has the maximum sum among all possible subarrays.



Input:

An integer array arr of length n where 1 ≤ n ≤ 10^5 and each element arr[i] is an integer.

Output:

An integer representing the sum of the subarray with the maximum sum. If all numbers are negative, the algorithm should handle that correctly by returning the largest single number or zero if the array is empty."""
def max_subarray_sum(arr):
    """
    Finds the sum of the subarray with the maximum sum.

    Parameters:
    arr (list): List of integers.

    Returns:
    int: The sum of the subarray with the maximum sum.
    """
    if not arr:
        return 0

    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum