#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'char_count' function below.
#
# The function is expected to return a DICTIONARY.
# The function accepts STRING str as parameter.
#

def char_count(str):
    # Write your code here
    freq = {}

    for c in str:
        if c != ' ':
            lower = c.lower()
            freq[lower] = freq.get(lower, 0) + 1

    return freq

if __name__ == '__main__':
    print("char_count('hello') ->", char_count('hello'))
    print("char_count('mississippi') ->", char_count('mississippi'))
