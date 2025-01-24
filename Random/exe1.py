"""
Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums."""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = n * (n  + 1)/ 2
        total_sum = sum(nums)
        return int(actual_sum - total_sum)
        

# another solution 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n        