'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 1
  Problem 2: Sharing Cookies

  Imagine you're an awesome babysitter and want to give the kids you're
  looking after some cookies as a snack. Each child `i` has a greed factor
  `g[i]`, which is the minimum size of a cookie that the child will be
  content with. Each cookie `j` has a cookie size `s[j]`. If `s[j] >= g[i]`,
  we can assign the cookie `j` to the child `i`, and the child will be
  content. If `s[j] < g[i]`, the child will not be content.

  Write a function `find_content_children()` that takes in the greed list
  `g` and the cookie size list `s` as parameters and maximizes the number of
  content children you are babysitting! The function returns

  Example 1:

  Write your solution for `find_content_children` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_content_children` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_content_children(s, g):
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

grade(find_content_children)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 1, 3], [1, 2, 3], expected=2)   # checks the value your code returns against this example
