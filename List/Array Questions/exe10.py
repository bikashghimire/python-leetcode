"""
Description:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique, and you may return the result in any order."""
def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    # TODO: Implement this function
    set1 = set(nums1)
    empty_set = set()
    for i in nums2:
        if i in set1:
            empty_set.add(i)
    return list(empty_set)
    
