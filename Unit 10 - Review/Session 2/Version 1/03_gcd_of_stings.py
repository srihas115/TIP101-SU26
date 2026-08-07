'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 1
    Problem 3: GCD of Strings

    For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s =
    t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or
    more times).

    Given two strings `str1` and `str2`, return *the largest string* `x` *such
    that* `x` *divides both* `str1` *and* `str2`.

    Write your solution for `gcd_of_stings` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `gcd_of_stings` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 
    input: str1 and str2
    output: largest string x s.t. x divides both str1 and str2
    core logic: 

Match:
    helper function to get gcd between str1 and str2

Plan:
    check if str1 + str2 is not the same as str2 + str1
        return an empty string, since there would be no way to have a common divisor
    
    
'''
def gcd(a, b):
    # use euclids algorithm
    pass

def gcd_of_stings(str1, str2):
    if str(str1) + str(str2) != str(str2) + str(str1):
        return False
    pass

'''
Example #1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

len str1 = 6
len str2 = 3

(-->) len str1 / len str2 = 2
(<--) str2 + str2 == str1



Example #2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

two pointer, go through str1 and str2
have a string that would keep track of the gcd somehow in a for loop


Example #3:
Input: st1 = "LEET", str2 = "CODE"
Output: ""


'''


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

grade(gcd_of_stings)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('ABCABC', 'ABC', expected='ABC')   # checks the value your code returns against this example
