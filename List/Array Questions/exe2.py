"""
Description:
Given a list of integers, write a function to find the sum of all the elements in the list.
"""
def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    # TODO: Implement this function
    add = 0
    for i in lst:
        add += i
        
    return add