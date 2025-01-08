"""

Remove Duplicates in a string
Problem Description:

You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string."""
def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    st = ""
    for i in s:
        if i not in st:
            st += i
     
    return st
            