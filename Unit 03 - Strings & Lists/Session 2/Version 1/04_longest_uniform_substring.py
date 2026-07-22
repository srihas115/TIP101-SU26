'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 2  ·  Version 1
    Problem 4: Longest Uniform Substring

    Write a function `longest_uniform_substring()` that takes in a string `s`
    and returns the length of the longest uniform substring. A uniform
    substring consists of a single repeated character.

    Write your solution for `longest_uniform_substring` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `longest_uniform_substring` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def longest_uniform_substring(s):
    pass

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", longest_uniform_substring(""))

print("Test 2 - single character")
print("  expected:", 1, "| got:", longest_uniform_substring("a"))

print("Test 3 - all-same-character string")
print("  expected:", 5, "| got:", longest_uniform_substring("aaaaa"))

print("Test 4 - longest run is at the end")
print("  expected:", 5, "| got:", longest_uniform_substring("abccccc"))


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

grade(longest_uniform_substring)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('aabbbbCdAA', expected=4)   # checks the value your code returns against this example
