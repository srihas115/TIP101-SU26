'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 2
  Problem 3: Evaluate Palindrome
==============================================================================
'''


def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s
