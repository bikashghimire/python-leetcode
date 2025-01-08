"""Count Vowels in a string
Problem Description:

You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count."""
def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    lt = "AEIOUaeiou"
    add = 0
    for i in s:
        if i in lt:
            add += 1
    return add
        
        
        
