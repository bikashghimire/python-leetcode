def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Implement the function logic
    for i in range(len(letters)):
        if letters[i] == target:
            return letters[i+1]
        else:
            return letters[0]
