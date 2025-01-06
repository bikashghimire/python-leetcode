"""
You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).
"""
def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    lt = []
    for i  in range(n):
        if i == 0 or i == n-1:
            lt.append('*' * n)
        else:
            lt.append('*' + ' ' * (n-2) + '*')
    return lt