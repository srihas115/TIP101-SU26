# using iterators
def valid_palindrome1(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            # return the check of the skipped character
            skip_left = s[start+1 : end+1]
            skip_right = s[start : end]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        start += 1
        end -= 1
    return True



# Using helper method
def valid_palindrome2(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return is_valid_palindrome_HELPER(s, start+1, end) or is_valid_palindrome_HELPER(s, start, end-1)
        start += 1
        end -= 1
    return True

# helper for valid_palindrome2(s)
def is_valid_palindrome_HELPER(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1 
    return True
    

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome1(s))
print(valid_palindrome1(s2))
print(valid_palindrome1(s3))

print()

print(valid_palindrome2(s))
print(valid_palindrome2(s2))
print(valid_palindrome2(s3))


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade, test

grade(valid_palindrome)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('aba', expected=True)   # checks the value your code returns against this example
