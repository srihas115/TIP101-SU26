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
    print("contains_duplicate([1, 2, 3, 1]) ->", contains_duplicate([1, 2, 3, 1]))
    print("contains_duplicate([1, 2, 3, 4]) ->", contains_duplicate([1, 2, 3, 4]))
