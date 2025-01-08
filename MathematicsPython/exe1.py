"""
Sum of N Even Natural Numbers
Problem Description:

You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ..."""
def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    lt = []
    add = 0
    for i in range(1,n+1):
        lt.append(i*2)
    for j in lt:
        add += j
    return add
        