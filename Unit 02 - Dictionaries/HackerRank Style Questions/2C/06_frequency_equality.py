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
    print("frequency_equality([1, 2, 2], [2, 1, 2]) ->", frequency_equality([1, 2, 2], [2, 1, 2]))
    print("frequency_equality([1, 2], [1, 1]) ->", frequency_equality([1, 2], [1, 1]))
