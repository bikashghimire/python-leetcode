"""
Words Frequency in a Sentence
Count Word Frequency

Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

Parameters:

sentence (str): The input sentence where you need to count the frequency of each word.

Returns:

A dictionary where the keys are words from the sentence and the values are their corresponding frequencies."""
def count_word_frequency(sentence):
    # Your code goes here
    s = sentence.split()
    di = {}
    for i in s:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    return di
