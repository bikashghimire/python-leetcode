"""
Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Input Parameters:

nums (List[int]): A list of integers where each integer is unique and in the range [0, n].

Output:


int: The missing number in the range [0, n]."""
def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    # TODO: Implement this function
    n = len(nums)
    actual_sum = n * (n + 1) / 2
    total_sum = sum(nums)
    return int(actual_sum - total_sum)
    
