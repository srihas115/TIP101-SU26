#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'contains_duplicate' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def contains_duplicate(nums):
    # Write your code here
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    for v in count_dict.values():
        if v >= 2:
            return True

    return False
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    temp = input()

    if len(temp) > 40:
        input_string = temp
        chunks = input_string.split(", ")
        list_of_lists = [list(map(int, chunk.split())) for chunk in chunks]
        result = [contains_duplicate(lst) for lst in list_of_lists]
    else:
        result = contains_duplicate([int(n) for n in temp.split()])

    fptr.write(str(result) + '\n')

    fptr.close()
