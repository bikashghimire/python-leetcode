"""
Count words in a string
Problem Description:

You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces."""
def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    count = 0
    word = False
    for char in s:
        if char !=' ':
            if not word:
                word = True
                count += 1
        else:
            word = False
    return count
