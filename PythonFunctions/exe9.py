"""
Rotate a List
Rotate a List (Without Slicing)

You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front."""
def rotate_list(nums, k):
    if not nums:
        return []
    n = len(nums)
    k = k % n  # Effective rotations needed
  
    
    for _ in range(k):
        last_element = nums.pop()  # Remove the last element
        nums.insert(0, last_element)  # Insert it at the front
    
    return nums

