"""
Description:
Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted in ascending order and then rotated at some pivot."""
def findMin(nums):
    # Implement your solution here
    minele = nums[0]
    for i in nums:
        if i < minele:
            minele = i
        else:
            minele = minele
    return minele