#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'frequency_greater_than_n' function below.
#
# The function is expected to return a DICTIONARY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER n
#

def frequency_greater_than_n(nums, n):
    # Write your code here
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    res_dict = {}
    for k, v in freq_dict.items():
        if v > n:
            res_dict[k] = v

    return res_dict

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    if len(t) > 65:
        chunks_in_range = t.split(", ")
        list_of_lists_in_range = [list(map(int, chunk.split())) for chunk in chunks_in_range]
        result = [frequency_greater_than_n(lst[1:], lst[0]) for lst in list_of_lists_in_range]
    else:
        temp = ([int(n) for n in t.split()])
        result = frequency_greater_than_n(temp[1:], temp[0])

    fptr.write(str(result) + '\n')

    fptr.close()
