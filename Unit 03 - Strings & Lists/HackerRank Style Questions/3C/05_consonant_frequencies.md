# Consonant Frequencies

Source: HackerRank Style Unit 3 Assessment, Version C

## Question

Write a function named consonant_frequencies that accepts a string as its input and returns a dictionary.
This dictionary should contain only consonants as keys and their frequencies as values. The counting
should be case-insensitive (i.e., 'B' and 'b' are considered the same), and white spaces, numbers, and
symbols should be ignored.
Constraints:
The input string may contain alphabets, numbers, and symbols.
Ignore all characters except consonants.
The function should handle case sensitivity by treating uppercase and lowercase consonants as the
same.

# Input: 'Fantastic 4!'
# Output: {'f': 1, 'n': 1, 't': 2, 's': 1, 'c': 1}
# Input: 'Hello World! 123'
# Output: {'h': 1, 'l': 3, 'w': 1, 'r': 1, 'd': 1}
