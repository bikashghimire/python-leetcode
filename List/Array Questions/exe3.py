"""
Description:
Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.
"""
def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # TODO: Implement this function
    left = 0
    right = len(lst) - 1
    
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True