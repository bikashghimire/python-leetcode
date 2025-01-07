def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    pattern = []
    # Generate the upper part of the diamond
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        pattern.append(spaces + stars + spaces)
    
    # Generate the lower part of the diamond (mirrored upper part)
    for i in range(n - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        pattern.append(spaces + stars + spaces)
    
    return pattern


