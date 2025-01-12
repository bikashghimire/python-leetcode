"""
Description:
Given a list of integers, write a function to find the maximum element in the list.
"""
def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    # TODO: Implement this function
    max_ele = lst[0]
    for i in lst:
        if i > max_ele:
            max_ele = i
    return max_ele