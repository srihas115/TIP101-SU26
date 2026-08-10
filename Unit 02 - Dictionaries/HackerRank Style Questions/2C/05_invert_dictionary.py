#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'invert_dictionary' function below.
#
# The function is expected to return an DICTIONARY.
# The function accepts DICTIONARY original as parameter.
#

def invert_dictionary(original):
    # Write your code here
    res = {}
    for k, v in original.items():
        res[v] = k
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    temp = input()

    if len(temp) > 115:
        def helper(inlist):
            original = {}
            for i in range(0, len(inlist), 2):
                key = f"{inlist[i]}"
                value = f"{inlist[i+1]}"
                original[key] = value
            return original
        chunks = temp.split(", ")
        list_of_lists = [list(map(str, chunk.split())) for chunk in chunks]
        result = [invert_dictionary(helper(lst)) for lst in list_of_lists]
    else:
        original = {}
        input_list = temp.split()

        for i in range(0, len(input_list), 2):
            key = f"{input_list[i]}"
            value = f"{input_list[i+1]}"
            original[key] = value

        result = invert_dictionary(original)

    fptr.write(str(result) + '\n')

    fptr.close()
