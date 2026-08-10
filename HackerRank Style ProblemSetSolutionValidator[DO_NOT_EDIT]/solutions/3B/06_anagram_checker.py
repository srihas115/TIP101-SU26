#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram_checker' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def anagram_checker(str1, str2):
    # Write your code here
    freq1 = {}
    for c in str1:
        if c != ' ':
            lower_c = c.lower()
            freq1[lower_c] = freq1.get(lower_c, 0) + 1

    freq2 = {}
    for c in str2:
        if c != ' ':
            lower_c = c.lower()
            freq2[lower_c] = freq2.get(lower_c, 0) + 1

    return freq1 == freq2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    def split(inlist):
        first = inlist[:(len(inlist) // 2)]
        second = inlist[(len(inlist) // 2):]
        return [first, second]

    if len(t) > 105:
        chunks = t.split(", ")
        list_of_lists = [list(map(str, chunk.split())) for chunk in chunks]
        result = [anagram_checker(" ".join(split(lst)[0]), " ".join(split(lst)[1])) for lst in list_of_lists]
    else:
        temp = t.split(',')
        str1 = str(temp[0])
        str2 = str(temp[1])
        result = anagram_checker(str1, str2)

    fptr.write(str(result) + '\n')

    fptr.close()
