#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'in_range' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER min_val
#  3. INTEGER max_val
#

def in_range(nums, min_val, max_val):
    # Write your code here
    res = []
    for num in nums:
        if num > min_val and num < max_val:
            res.append(num)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    if len(t) > 60:
        input_string_in_range = t
        chunks_in_range = input_string_in_range.split(", ")
        list_of_lists_in_range = [list(map(int, chunk.split())) for chunk in chunks_in_range]
        result = [in_range(lst[2:], lst[0], lst[1]) for lst in list_of_lists_in_range]

    else:
        temp = [int(n) for n in t.split()]
        result = in_range(temp[2:], temp[0], temp[1])

    fptr.write(str(result) + '\n')

    fptr.close()
