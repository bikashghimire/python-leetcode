"""
Selection Sort
Selection Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.


"""
def selection_sort(myArray):
    for i in range(len(myArray)):
        min_num = i
        for j in range(i+1, len(myArray)):
            if myArray[j] < myArray[min_num]:
                myArray[j], myArray[min_num] = myArray[min_num], myArray[j]
    return myArray