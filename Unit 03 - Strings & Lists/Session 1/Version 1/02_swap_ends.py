'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 1  ·  Version 1
  Problem 2: Swap Ends

  Write a function `swap_ends()` that accepts a string `my_str` as a
  parameter and returns a new string where the first and last characters
  from `my_str` are swapped.

  Write your solution for `swap_ends` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `swap_ends` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def swap_ends(my_str):
    pass

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single character string (first and last are the same char)")
print("  expected:", "a", "| got:", swap_ends("a"))

print("Test 2 - empty string")
print("  expected:", "", "| got:", swap_ends(""))

print("Test 3 - two character string")
print("  expected:", "ba", "| got:", swap_ends("ab"))

print("Test 4 - all-same-character string")
print("  expected:", "zzzz", "| got:", swap_ends("zzzz"))

print("Test 5 - mixed case string")
print("  expected:", "eodC", "| got:", swap_ends("CodE"))

print("Test 6 - string with punctuation/whitespace ends")
print("  expected:", " hi!", "| got:", swap_ends("! hi "))


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

grade(swap_ends)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('boat', expected='toab')   # checks the value your code returns against this example
