'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 1  ·  Version 3
    Problem 6: Odd Keys Even Values

    Write a function `odd_keys_even_values()` that takes in `dictionary` as a
    parameter, a dictionary with integer keys and values. The function returns
    a list of keys that are odd where their corresponding values are even.

    Write your solution for `odd_keys_even_values` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `odd_keys_even_values` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def odd_keys_even_values(dictionary):
    pass

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dict")
print("  expected:", [], "| got:", odd_keys_even_values({}))

print("Test 2 - all keys even (none qualify)")
print("  expected:", [], "| got:", odd_keys_even_values({2: 4, 4: 8}))

print("Test 3 - odd key but odd value (excluded)")
print("  expected:", [], "| got:", odd_keys_even_values({3: 5}))

print("Test 4 - negative odd key with even value")
print("  expected:", [-3], "| got:", odd_keys_even_values({-3: 2}))

print("Test 5 - single qualifying pair")
print("  expected:", [7], "| got:", odd_keys_even_values({7: 10}))


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

grade(odd_keys_even_values)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({1: 2, 2: 6, 3: 5, 4: 4, 5: 8}, expected=[1, 5])   # checks the value your code returns against this example
