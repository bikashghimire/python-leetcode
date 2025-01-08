"""
Problem Description:

You are given a positive integer num. Your task is to check whether num is a perfect square or not. A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise."""
def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    return int(num**0.5)*int(num**0.5) == num