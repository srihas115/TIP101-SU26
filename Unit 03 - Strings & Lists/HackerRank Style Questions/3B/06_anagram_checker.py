#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram_checker' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def anagram_checker(str1, str2):
    # Write your code here
    freq1 = {}
    for c in str1:
        if c != ' ':
            lower_c = c.lower()
            freq1[lower_c] = freq1.get(lower_c, 0) + 1

    freq2 = {}
    for c in str2:
        if c != ' ':
            lower_c = c.lower()
            freq2[lower_c] = freq2.get(lower_c, 0) + 1

    return freq1 == freq2

if __name__ == '__main__':
    print("anagram_checker('listen', 'silent') ->", anagram_checker('listen', 'silent'))
    print("anagram_checker('hello', 'world') ->", anagram_checker('hello', 'world'))
