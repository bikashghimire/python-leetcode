"""
Merge Dictionaries with Common Keys
Problem Description

Merge Dictionaries with Overlapping Keys

Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. If a key appears in more than one dictionary, sum up their values.

Parameters:

dicts (list): A list of dictionaries where keys might overlap.

Returns:

A single dictionary where values for overlapping keys are summed."""
def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    di = {}
    for i in dicts:
        for keys,values in i.items():
            if keys in di:
                di[keys] += values
            else:
                di[keys] = values
    return di
        
        
