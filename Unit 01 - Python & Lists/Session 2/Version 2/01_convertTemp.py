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
  kelvin = round((celsius + 273.15), 2)
  fahrenheit = round(((celsius * 1.8) + 32), 2)

  ans = []

  ans.append(kelvin)
  ans.append(fahrenheit)
  
  return ans

temperatures = convertTemp(23.00)
print(temperatures)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - celsius is 0")
print("  expected:", [273.15, 32.0], "| got:", convertTemp(0))

print("Test 2 - celsius is 100 (boiling point)")
print("  expected:", [373.15, 212.0], "| got:", convertTemp(100))

print("Test 3 - matches example")
print("  expected:", [296.15, 73.4], "| got:", convertTemp(23.00))

print("Test 4 - decimal celsius value")
print("  expected:", [309.75, 97.88], "| got:", convertTemp(36.6))


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
