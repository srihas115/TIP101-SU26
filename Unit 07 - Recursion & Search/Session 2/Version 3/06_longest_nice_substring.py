'''
==============================================================================
    Unit 7: Recursion & Search  ·  Session 2  ·  Version 3
    Problem 6: What a Nice String

    A string `s` is **nice** if, for every letter of the alphabet that `s`
    contains, it appears **both** in uppercase and lowercase. For example,
    `"abABB"` is nice because `'A'` and `'a'` appear, and `'B'` and `'b'`
    appear. However, `"abA"` is not because `'b'` appears, but `'B'` does not.

    Using the divide and conquer approach, write a function
    `longest_nice_substring()` that takes in a string `s` and returns the
    longest **substring** of `s` that is **nice**. If there are multiple,
    return the substring of the **earliest** occurrence. If there are none,
    return an empty string.

    Write your solution for `longest_nice_substring` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `longest_nice_substring` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def longest_nice_substring(s):
    pass

# Example Input: s = "YazaAay"


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

grade(longest_nice_substring)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('YazaAay', expected='aAa')   # checks the value your code returns against this example
