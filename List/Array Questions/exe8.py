"""
Description:
Write a function that checks whether the given array is sorted in non-decreasing order. The array is considered sorted if every element is less than or equal to the next element.

"""
def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    # TODO: Implement this function
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            return False
    return True
