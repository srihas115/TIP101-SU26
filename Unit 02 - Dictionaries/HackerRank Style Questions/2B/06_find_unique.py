#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_unique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def find_unique(nums):
    # Write your code here
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    for k, v in freq_dict.items():
        if v == 1:
            return k

    return None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    temp = input()

    if len(temp) > 120:
        chunks = temp.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]
        result = [find_unique(lst) for lst in list_of_lists]
    else:
        result = find_unique([int(n) for n in temp.split()])

    fptr.write(str(result) + '\n')

    fptr.close()
