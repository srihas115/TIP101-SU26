'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 1
  Problem 3: Print Pair

  Write a function `print_pair()` that takes in a dictionary `dictionary`
  and a key `target` as parameters. The function looks for the `target` and
  when found, it prints the key and it's associated value as `"Key: <key>"`
  followed by `"Value: <value>"`. If `target` is not in `dictionary`, print
  `"That pair does not exist!"`.

  Write your solution for `print_pair` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `print_pair` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def print_pair(dictionary, target):
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

grade(print_pair)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'spongebob': 'squarepants', 'patrick': 'star'}, 'patrick', expected='Key: patrick\nValue: star')   # checks the printed output against this example
