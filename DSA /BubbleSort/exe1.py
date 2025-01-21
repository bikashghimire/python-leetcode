"""
Bubble Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Bubble Sort algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.
"""
def bubble_sort(lst):
    # Your code goes here
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j],lst[j+1] = lst[j +1], lst[j]
    return lst
