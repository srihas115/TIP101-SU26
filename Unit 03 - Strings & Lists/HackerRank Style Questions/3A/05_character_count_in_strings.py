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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()

    if len(string) > 55:
        chunks = string.split(", ")
        list_of_lists = [list(map(str, chunk.split())) for chunk in chunks]
        result = [char_count(" ".join(lst)) for lst in list_of_lists]
    else:
        result = char_count(string)

    fptr.write(str(result) + '\n')

    fptr.close()
