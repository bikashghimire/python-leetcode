"""Write a function to merge two dictionaries."""
def merge_dictionaries(dict1, dict2):
    return (dict1 | dict2)

""" write a function to check if John is making progress in his workout"""
def is_johnny_making_progress(day1, day2, day3):
    if day1 < day2 and day2 < day3 and day1 < day3:
        return True
    return False

"""Write a function to if the number is weird"""
def is_weird(n):
    if n % 2 != 0:
        return 'Weird'
    elif n % 2 == 0 and n > 20:
        return 'Not Weird'
    elif n % 2 == 0 and 2 < n < 5:
        return 'Not Weird'
    elif n % 2 == 0 and 6 < n < 20:
        return 'Weird'
    
""" Write a function to check if a number is pandigital"""
def is_pandigital(n):
    return len(set(str(n))) == 10

"""Write a function to find the fulcrum of a list"""
def find_fulcrum(lst):
    l = len(lst)
    mid = l // 2
    first = lst[:mid]
    last = lst[mid + 1:]
    if sum(first) == sum(last):
        return lst[mid]


