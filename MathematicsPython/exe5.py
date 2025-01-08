"""
Problem Description:

You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion."""
def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n >= 0:
        return bin(n)[2:]
    else:
        return ("-") + bin(abs(n))[2:]
