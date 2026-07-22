'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 3
  Problem 6: Flowerbed

  Imagine you have a flowerbed in which some of the plots are planted, and
  some are not. Flowers cannot be planted in adjacent plots.

  Write a function `can_place_flowers()` that takes in an integer list
  `flowerbed` containing 0's and 1's, (*where 0 is an empty plot and 1 is a
  planted plot*) and an integer `n` that represents the number of new
  flowers wanting to be planted as parameters. The function should return
  `True` if `n` new flowers can be planted in the flowerbed without
  violating the no-adjacent-flowers rule and `False` otherwise.

  Write your solution for `can_place_flowers` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `can_place_flowers` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def can_place_flowers(flowerbed, n):
    pass

flowerbed = [1,0,0,0,1]
approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)
print(approved)
print(approved2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 0 (always possible, trivially true)")
print("  expected:", True, "| got:", can_place_flowers([1,1,1], 0))

print("Test 2 - all-zero flowerbed, maximum capacity")
print("  expected:", True, "| got:", can_place_flowers([0,0,0,0,0], 3))

print("Test 3 - no room at all, n is 1")
print("  expected:", False, "| got:", can_place_flowers([1,1,1], 1))

print("Test 4 - single empty plot")
print("  expected:", True, "| got:", can_place_flowers([0], 1))


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

grade(can_place_flowers)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 0, 0, 0, 1], 1, expected=True)   # checks the value your code returns against this example
