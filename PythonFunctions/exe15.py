"""
Check if List is Subset of another List
Check if a List is a Subset of Another List (Brute Force Approach)

You are given two lists of integers. Write a Python program that checks whether the first list is a subset of the second list using a brute-force approach, without using the in keyword. A list is considered a subset if all elements of the first list are present in the second list.

Parameters:

lst1 (List of integers): The first list, which is being checked as a subset.

lst2 (List of integers): The second list, which is the list to compare against.

Returns:

"""
def is_subset(lst1, lst2):
    for element in lst1:
        found = False
        for i in lst2:
            if i == element:
                found = True
                break
        if not found:
            return False
    return True