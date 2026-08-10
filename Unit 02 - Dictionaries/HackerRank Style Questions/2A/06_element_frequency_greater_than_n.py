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
    print("frequency_greater_than_n([1, 1, 2, 3], 1) ->", frequency_greater_than_n([1, 1, 2, 3], 1))
    print("frequency_greater_than_n([1, 2, 3], 2) ->", frequency_greater_than_n([1, 2, 3], 2))
