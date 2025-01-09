def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    # Your code here
    max_length = 0
    current_length = 0
    for i in range(len(s)):
        if s[i] != ' ':
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
        if current_length > max_length:
            max_length = current_length

    return max_length