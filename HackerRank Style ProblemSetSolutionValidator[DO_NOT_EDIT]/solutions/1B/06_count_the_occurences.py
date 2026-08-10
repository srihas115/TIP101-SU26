#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'count_occurrences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY lst
#  2. INTEGER val
#

def count_occurrences(lst, val):
    # Write your code here
    count = 0
    for num in lst:
        if val == num:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    if len(t) > 70:
        input_string_in_range = t
        chunks_in_range = input_string_in_range.split(", ")
        # Parsing each chunk into lists of integers, excluding the first and last numbers which represent min and max values
        list_of_lists_in_range = [list(map(int, chunk.split())) for chunk in chunks_in_range]
        result = [count_occurrences(lst[1:], lst[0]) for lst in list_of_lists_in_range]
    else:
        temp = [int(n) for n in t.split()]
        result = count_occurrences(temp[1:], temp[0])

    fptr.write(str(result) + '\n')

    fptr.close()
