'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 2
  Problem 3: Longest Common Prefix

  Write a function `longest_common_prefix()` that takes in a list of strings
  `strings` as a parameter. The function returns the longest common prefix
  (*not substring*) of **all** strings and if there are none, it returns an
  empty string `""`.

  Write your solution for `longest_common_prefix` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `longest_common_prefix` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def longest_common_prefix(strings):
    pass  # replace this line with your solution













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

grade(longest_common_prefix)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['flower', 'flow', 'flight'], expected='fl')   # checks the value your code returns against this example
