#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'count_unique_words' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING str as parameter.
#

def count_unique_words(str):
    # Write your code here
    lst = str.lower().split()
    return len(set(lst))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()

    if len(string) > 565:
        chunks = string.split(", ")
        list_of_lists = [list(map(str, chunk.split())) for chunk in chunks]
        result = [count_unique_words(" ".join(lst)) for lst in list_of_lists]
    else:
        result = count_unique_words(string)

    fptr.write(str(result) + '\n')

    fptr.close()
