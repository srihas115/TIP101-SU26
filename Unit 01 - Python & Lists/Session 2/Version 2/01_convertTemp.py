'''
==============================================================================
  Unit 1: Python & Lists  ·  Session 2  ·  Version 2
  Problem 1: Convert Temperature

  Write a function `convertTemp()` that takes in `celsius` as a parameter,
  which denotes the temperature in celsius. The variable is a non-negative
  floating point number rounded to two decimal places. In the function,
  convert `celsius` into **Kelvin** and **Fahrenheit** and return the list
  `ans`, in which `ans = [kelvin, fahrenheit]`.

  **Note that:** - `Kelvin = Celsius + 273.15` - `Fahrenheit = Celsius *
  1.80 + 32.00`

  Write your solution for `convertTemp` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `convertTemp` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def convertTemp(celsius):
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

grade(convertTemp)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(23.0, expected=[296.15, 73.4])   # checks the value your code returns against this example
