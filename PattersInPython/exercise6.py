def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    # Your code here
    pyramid = []
    for i in range(n):
        num_stars = 2 * i + 1
        num_spaces = (2 * n - 1 - num_stars) // 2
        line = ' ' * num_spaces + '*' * num_stars + ' ' * num_spaces
        pyramid.append(line)
    return pyramid
