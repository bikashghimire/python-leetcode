"""
Merge Multiple Dictionaries
Merge Three Dictionaries

Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

Parameters:

dict1 (Dictionary): The first dictionary to be merged.

dict2 (Dictionary): The second dictionary to be merged.

dict3 (Dictionary): The third dictionary to be merged.

Returns:

A single dictionary containing all key-value pairs from the three input dictionaries."""
def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    lt = {}
    
    for key, value in dict1.items():
        lt[key] = value
    for key, value in dict2.items():
        lt[key] = value
    for key, value in dict3.items():
        lt[key] = value
    
    return lt
        
