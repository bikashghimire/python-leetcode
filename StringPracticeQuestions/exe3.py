import re
def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    normalized_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    r_s = ""
    for i in normalized_s:
        r_s = i + r_s
    return normalized_s == r_s
