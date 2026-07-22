'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 1  ·  Version 1
    Problem 4: Reverse String

    Write a function `reverse_string()` that takes a string `my_str` as a
    parameter and returns the string reversed.

    Write your solution for `reverse_string` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `reverse_string` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def reverse_string(my_str):
    pass

my_str = "live"
print(reverse_string(my_str))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", "", "| got:", reverse_string(""))

print("Test 2 - single character string")
print("  expected:", "x", "| got:", reverse_string("x"))

print("Test 3 - all-same-character string")
print("  expected:", "mmmm", "| got:", reverse_string("mmmm"))

print("Test 4 - mixed case string")
print("  expected:", "EdoC", "| got:", reverse_string("CodE"))

print("Test 5 - string with punctuation and whitespace")
print("  expected:", "!dlrow ,olleH", "| got:", reverse_string("Hello, world!"))

print("Test 6 - palindrome string reverses to itself")
print("  expected:", "racecar", "| got:", reverse_string("racecar"))


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

grade(reverse_string)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('live', expected='evil')   # checks the value your code returns against this example
