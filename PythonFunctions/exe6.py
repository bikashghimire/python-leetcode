"""
Count Number of Odd and Even Elements in a List
Count Even and Odd Numbers in a List

You are given a list of integers. Write a Python program that counts and returns the number of even and odd numbers in the list.

"""
def count_even_odd(lst):
    # Your code goes here
    even_count = 0
    odd_count = 0
    for i in lst:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
