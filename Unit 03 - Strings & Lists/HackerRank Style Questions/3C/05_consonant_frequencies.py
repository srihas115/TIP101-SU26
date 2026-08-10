#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'consonant_frequencies' function below.
#
# The function is expected to return a DICTIONARY.
# The function accepts STRING str as parameter.
#

def consonant_frequencies(str):
    # Write your code here
    lower_str = str.lower()
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    freq = {}

    for c in lower_str:
        if c != ' ' and c.isalpha() and (c not in vowels):
            freq[c] = freq.get(c, 0) + 1

    return freq

if __name__ == '__main__':
    print("consonant_frequencies('banana') ->", consonant_frequencies('banana'))
    print("consonant_frequencies('codepath') ->", consonant_frequencies('codepath'))
