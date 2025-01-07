"""
Program to Reverse a List
Reverse a List (Non-Slicing Approach)

You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]). The program should return the reversed list."""
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        # Swap the elements at the left and right pointers
        lst[left] = lst[right]
        lst[right] = lst[left]
        # Move the pointers
        left += 1
        right -= 1
    return lst
