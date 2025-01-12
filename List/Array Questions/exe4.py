"""Description:
Given a list of integers, write a function to reverse the order of elements in the list."""
def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    
    left = 0
    right = len(lst) -1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -=1
    return lst