"""
Reverse a string
Problem Description:

You are given a string s. Your task is to return the reversed version of the string.



Input:

A single string s, where the length of s is between 1 and 1000.



Output:

A single string that is the reverse of the input string."""
def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here
    add = ""
    for i in s:
        add = i + add
    return add
    
