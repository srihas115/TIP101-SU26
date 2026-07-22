'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 1
  Problem 3: Shuffle Merge

  Given the heads of two singly linked lists of integers, merge their nodes
  to make one list, taking nodes alternately between the two lists. If
  either list runs out of elements before the other, all nodes from the list
  with remaining nodes should be appended onto the end of the merged list.
  Return the head of the merged list.

  Write your solution for `shuffle_merge` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `shuffle_merge` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def shuffle_merge(head_a, head_b):
    pass


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

grade(shuffle_merge)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3], [4, 5, 6], expected=[1, 4, 2, 5, 3, 6])   # checks the value your code returns against this example
