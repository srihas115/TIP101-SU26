#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'ransom_note' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING message
#  2. STRING magazine
#

def ransom_note(message, magazine):
    # Write your code here
    freq_message = {}
    for c in message:
        freq_message[c] = freq_message.get(c, 0) + 1

    freq_magazine = {}
    for c in magazine:
        freq_magazine[c] = freq_magazine.get(c, 0) + 1

    for k, v in freq_message.items():
        if v != freq_magazine.get(k, 0):
            return False

    return True

if __name__ == '__main__':
    print("ransom_note('abc', 'abc') ->", ransom_note('abc', 'abc'))
    print("ransom_note('aa', 'ab') ->", ransom_note('aa', 'ab'))
