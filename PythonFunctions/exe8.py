"""
Merge two Sorted List
Merge Two Sorted Lists

You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order."""
def merge_two_sorted_lists(list1, list2):
    i = 0
    j = 0
    lt = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            lt.append(list1[i])
            i += 1  # Increment i
        else:
            lt.append(list2[j])
            j += 1  # Increment j
    
    # Add remaining elements from list1
    while i < len(list1):
        lt.append(list1[i])
        i += 1
    
    # Add remaining elements from list2
    while j < len(list2):
        lt.append(list2[j])
        j += 1
    
    return lt
