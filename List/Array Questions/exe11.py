"""
Description:
Given a binary array nums, return the maximum number of consecutive 1s in the array."""
def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    add = 0
    max_count = 0

    for i in nums:
        if i == 1:
            add += 1
        else:
            max_count = max(max_count, add)
            add = 0
            

    return max(max_count, add)
