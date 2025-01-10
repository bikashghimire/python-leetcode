"""Description:
Given a sorted array that has been rotated, find the index of a given target value. The array was originally sorted in ascending order and then rotated at some pivot."""
def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = nums[mid]
        
        # If we found the target
        if mid_value == target:
            return mid
        
        # Check if the left half is sorted
        if nums[left] <= mid_value:
            # If the target is within the range of the left half
            if nums[left] <= target < mid_value:
                right = mid - 1  # Search in the left half
            else:
                left = mid + 1  # Search in the right half
        else:
            # The right half must be sorted
            if mid_value < target <= nums[right]:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
    
    return -1  # If the target is not found
