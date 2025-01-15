"""
Problem Description:

You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on."""
def floyds_triangle(n):
    result = []
    current_num = 1  # Start with the first natural number
    for row in range(1, n + 1):  # For each row from 1 to n
        # Generate a row with `row` numbers
        current_row = " ".join(str(current_num + i) for i in range(row))
        result.append(current_row)
        current_num += row  # Update the starting number for the next row
    return result

# Example usage:
n = 5
print("\n".join(floyds_triangle(n)))
