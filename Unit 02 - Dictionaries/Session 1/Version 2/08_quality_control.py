'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 1  ·  Version 2
    Problem 8: Quality Control

    Write a function `quality_control()` that takes in a dictionary
    `product_scores` and an integer `threshold` as parameters. The dictionary
    `product_scores` has key-value pairs that represent a product ID and its
    quality rating. If the product has a score greater than or equal to
    `threshold`, the function categorizes it as a `"pass"`. If the product has
    a score less than `threshold`, the function categorizes it as a `"fail"`.
    The function returns a new dictionary where the key-value pair is the
    product ID and whether it is a `"pass"` or `"fail"`.

    Write your solution for `quality_control` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `quality_control` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def quality_control(product_scores, threshold):
    pass

product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(product_scores, threshold))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty product_scores dictionary")
print("  expected:", {}, "| got:", quality_control({}, 60))

print("Test 2 - single product exactly at threshold (>= threshold is a pass)")
print("  expected:", {"x0123": "pass"}, "| got:", quality_control({"x0123": 60}, 60))

print("Test 3 - all products pass")
print("  expected:", {"x0123": "pass", "x0124": "pass"}, "| got:", quality_control({"x0123": 80, "x0124": 90}, 60))

print("Test 4 - all products fail")
print("  expected:", {"x0123": "fail", "x0124": "fail"}, "| got:", quality_control({"x0123": 10, "x0124": 20}, 60))

print("Test 5 - all scores equal, at the threshold")
print("  expected:", {"x0123": "pass", "x0124": "pass"}, "| got:", quality_control({"x0123": 60, "x0124": 60}, 60))

print("Test 6 - threshold of 0 (all scores pass)")
print("  expected:", {"x0123": "pass"}, "| got:", quality_control({"x0123": 0}, 0))


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

grade(quality_control)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'x0123': 75, 'x0124': 40, 'x0125': 90, 'x0126': 55}, 60, expected={'x0123': 'pass', 'x0124': 'fail', 'x0125': 'pass', 'x0126': 'fail'})   # checks the value your code returns against this example
