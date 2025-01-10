"""
Description:
Given an array of integers nums sorted in non-decreasing order, and an integer target, find the starting and ending position of the given target value. If target is not found in the array, return [-1, -1]."""
def searchRange(nums, target):
    def left_search(nums, target):
        left = 0
        right = len(nums) -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left
        
    def right_search(nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid -1
        return right
    
    leftIndex = left_search(nums, target)
    if leftIndex == len(nums) or  nums[leftIndex] != target:
        return [-1,-1]
    rightindex = right_search(nums, target)
    return [leftIndex, rightindex]