"""
Check if all elements in a list are Unique
Check if All Elements in a List are Unique

You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False."""
def check_unique(lst):
    # Your code goes here
    ls = []
    for i in lst:
        if i not in ls:
            ls.append(i)
    return lst == ls