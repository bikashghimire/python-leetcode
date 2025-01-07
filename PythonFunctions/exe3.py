"""Remove Duplicate in a List
Remove Duplicates from a List

You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained."""
def remove_duplicates(lst):
    # Your code goes here
    ls = []
    for i in lst:
        if i not in ls:
            ls.append(i)

    return ls
