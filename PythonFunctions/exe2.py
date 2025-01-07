"""
Largest Element in a List
Find the Largest Element in a List

Write a Python function that finds and returns the largest element in a given list of integers."""
def find_largest(numbers):
    # Your code goes here
    max_number = numbers[0]
    for i in numbers:
        if i > max_number:
            max_number = i
    return max_number
        
        