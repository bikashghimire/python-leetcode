"""Problem Description:

You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself. Return True if the number is prime, and False otherwise."""
def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # Eliminate other even numbers
        return False
    
    # Check divisors from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True
    
