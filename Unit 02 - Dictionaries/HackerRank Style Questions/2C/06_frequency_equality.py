#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'frequency_equality' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY lst1
#  2. INTEGER_ARRAY lst2
#

def frequency_equality(lst1, lst2):
    # Write your code here
    freq1 = {}
    for num in lst1:
        freq1[num] = freq1.get(num, 0) + 1

    freq2 = {}
    for num in lst2:
        freq2[num] = freq2.get(num, 0) + 1

    return freq1 == freq2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    if len(t) > 140:
        chunks = t.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]

        def helper(inlist):
            temp = [int(n) for n in inlist]
            lst1 = temp[:(len(temp) // 2)]
            lst2 = temp[(len(temp) // 2):]
            return [lst1, lst2]

        result = [frequency_equality(helper(lst)[0], helper(lst)[1]) for lst in list_of_lists]
    else:
        temp = [int(n) for n in t.split()]
        lst1 = temp[:(len(temp) // 2)]
        lst2 = temp[(len(temp) // 2):]
        result = frequency_equality(lst1, lst2)

    fptr.write(str(result) + '\n')

    fptr.close()
