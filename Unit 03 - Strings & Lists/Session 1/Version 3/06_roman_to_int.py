'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 1  ·  Version 3
  Problem 6: Roman to Integer

  Roman Numerals are represented by seven different symbols (`I`, `V`, `X`,
  `L`, `C`, `D`, and `M`) and have these corresponding values:

  `I = 1` `V = 5` `X = 10` `L = 50` `C = 100` `D = 500` `M = 1000`

  For example, `2` is written as `II`, which is just two ones added
  together. `12` is written as `XII`, which is simply `X + II`. The number
  `27` is written as `XXVII`, which is `XX + V + II`.

  Roman numerals are usually written largest to smallest from left to right.
  However, the numeral for `4` is not `IIII`. Instead, the number `4` is
  written as `IV`.

  Because the `I` is before the `V`, we subtract it to equal `4`. The same
  principle applies to the number `9`, which is written as `IX`. There are
  six instances where subtraction is used: - `I` can be placed before `V`
  (5) and `X` (10) to make `4` and `9` - `X` can be placed before `L` (50)
  and `C` (100) to make `40` and `90` - `C` can be placed before `D` (500)
  and `M` (1000) to make `400` and `900`

  Write a function `roman_to_int()` that takes in a string `s` that makes up
  a roman numeral. The function should return the integer value of `s`.

  Write your solution for `roman_to_int` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `roman_to_int` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def roman_to_int(s):
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

grade(roman_to_int)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('XL', expected=40)   # checks the value your code returns against this example
