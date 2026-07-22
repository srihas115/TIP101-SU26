'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 1
  Problem 2: Best Time to Buy & Sell Stock

  You are given a list of integers `prices` where `prices[i]` is the price
  of a given stock on the `ith` day.

  You want to maximize your profit by choosing a **single day** to buy one
  stock and choosing a **different day in the future** to sell that stock.

  Return *the maximum profit you can achieve from this transaction*. If you
  cannot achieve any profit, return `0`.

  Write your solution for `max_profit` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `max_profit` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def max_profit(prices):
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

grade(max_profit)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([7, 1, 5, 3, 6, 4], expected=5)   # checks the value your code returns against this example
