#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'is_palindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING string as parameter.
#

def is_palindrome(string):
    # Write your code here
    left = 0
    right = len(string) - 1
    string = string.lower()

    while left < right:
        while left < right and not string[left].isalpha():
            left += 1
        while left < right and not string[right].isalpha():
            right -= 1

        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()

    if len(string) > 100:
        chunks = string.split(", ")
        list_of_lists = [list(map(str, chunk.split())) for chunk in chunks]
        result = [is_palindrome(" ".join(lst)) for lst in list_of_lists]
    else:
        result = is_palindrome(string)

    fptr.write(str(result) + '\n')

    fptr.close()
