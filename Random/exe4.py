"""
Write a function to check if a number is abundant or not.
"""
def is_abundant(n):
    ls = []
    for i in range(1,n):
        if n % i == 0:
            ls.append(i)
    add = 0
    for j in ls:
        add += j
    if n > add:
        return False
    return True