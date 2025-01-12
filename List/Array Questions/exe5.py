"""Description:
Given a list of integers and an integer D, write a function to rotate the list to the left by D positions."""
def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # TODO: Implement this function
    D = D % len(ARR)  # In case d is greater than the length of the list
    return ARR[D:] + ARR[:D]