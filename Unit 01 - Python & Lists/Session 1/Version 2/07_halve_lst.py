'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 1  ·  Version 2
  Problem 7: Unscramble and Divide

  Given the following lines of code, work with your group members to place
  the lines in order to write and call a function that divides each value in
  an input list by 2.

  a. `result = []` b. `for number in lst:` c. `result.append(halved)` d.
  `halved = number/2` e. `halve_lst([2,4,6,8])` f. `return result` g. `def
  halve_lst(lst):`

  Example Output: `[1,2,3,4]`

  Write your solution for `halve_lst` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `halve_lst` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def halve_lst(lst):
    result = []
    for number in lst:
        halved = number / 2
        # result.append(halved)
        result.append(halved) # should be int(halved))
    return result

print(halve_lst([2,4,6,8]))


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

grade(halve_lst)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 4, 6, 8], expected=[1.0, 2.0, 3.0, 4.0])   # checks the value your code returns against this example
