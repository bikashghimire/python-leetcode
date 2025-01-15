def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    # TODO: Implement this function
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    for i in range(pos, len(nums)):
        nums[i] = 0
