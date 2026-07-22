'''
==============================================================================
  Unit 6: Linked Lists II  ·  Session 1  ·  Version 3
  Problem 6: Reverse Them, K?

  Given the head of a singly linked list and an integer k, reverse the first
  k elements of the linked list. Return the new head of the linked list. If
  k is larger than the length of the list, reverse the entire list.

  Evaluate the time and space complexity of your solution. Define your
  variables and provide a rationale for why you believe your solution has
  the stated time and space complexity.

  Write your solution for `reverse_first_k` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `reverse_first_k` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



def reverse_first_k(head, k):
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

grade(reverse_first_k)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 4, 5], 3, expected=[3, 2, 1, 4, 5])   # checks the value your code returns against this example
