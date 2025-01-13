"""Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeroes.

Write a function to increment the large integer by one and return the resulting array of digits."""
def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # TODO: Implement this function
    # Time complexity is O(n * n)
    st = ""
    for i in digits:
        st += str(i)
    add = int(st) + 1
    ls = []
    for j in str(add):
        ls.append(int(j))
    return ls


# Another solution 
# Time complexity is O(n)
def plus_one(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        digits[i] += carry
        if digits[i] < 10:
            carry = 0
            break
        digits[i] = 0
    if carry:
        digits.insert(0, 1)
    return digits
