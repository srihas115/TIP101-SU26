'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 1
  Problem 4: Keys Versus Values

  Write a function `keys_v_values()` that takes in a dictionary `dictionary`
  whose keys and values are both integers. *Using at least one loop*, the
  function should find the sum of all keys in the dictionary and the sum of
  all values. If the sum of all keys is greater than the sum of all values,
  the function should return the string `"keys"`. If the sum of all values
  is greater than the sum of all keys, the function should return the string
  `"values"`. If keys and values have equal sums, the function should return
  the string `"balanced"`.

  Write your solution for `keys_v_values` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `keys_v_values` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def keys_v_values(dictionary):
    sum_keys = 0
    sum_vals = 0
    for k, v in dictionary.items():
        sum_keys += k
        sum_vals += v
    
    if sum_keys > sum_vals:
        return "keys"
    elif sum_keys < sum_vals:
        return "values"
    else:
        return "balanced"        

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dictionary (both sums are 0)")
print("  expected:", "balanced", "| got:", keys_v_values({}))

print("Test 2 - single key-value pair, equal key and value")
print("  expected:", "balanced", "| got:", keys_v_values({5: 5}))

print("Test 3 - keys sum greater than values sum")
print("  expected:", "keys", "| got:", keys_v_values({10: 1, 20: 2}))

print("Test 4 - values sum greater than keys sum")
print("  expected:", "values", "| got:", keys_v_values({1: 10, 2: 20}))

print("Test 5 - negative numbers, keys sum greater than values sum")
print("  expected:", "keys", "| got:", keys_v_values({-1: -5}))

print("Test 6 - all values equal across multiple keys, sums balanced")
print("  expected:", "balanced", "| got:", keys_v_values({1: 2, 2: 1}))


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

grade(keys_v_values)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, expected='values')   # checks the value your code returns against this example
