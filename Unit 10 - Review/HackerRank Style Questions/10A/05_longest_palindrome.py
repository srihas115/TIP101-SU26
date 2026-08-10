#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longest_palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def longest_palindrome(s):
    # Write your code here
    freq_dict = {}
    for c in s:
        freq_dict[c] = freq_dict.get(c, 0) + 1

    length = 0
    has_odd = False
    for c in freq_dict.values():
        length += (c // 2) * 2
        if c % 2 == 1:
            has_odd = True

    if has_odd:
        length += 1

    return length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = longest_palindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
