'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 2  ·  Version 2
    Problem 7: Good Pairs

    Write a function `num_identical_pairs()` that takes in a list of integers
    `nums` and returns the number of **good pairs**. A pair `(i, j)` is called
    **good** if `nums[i] == nums[j]` and `i` < `j`.

    Write your solution for `num_identical_pairs` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `num_identical_pairs` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def num_identical_pairs(nums):
    pass

nums = [1,2,3,1,1,3]
print(num_identical_pairs(nums))

nums = [1,2,3]
print(num_identical_pairs(nums))

nums = [1,1,1,1]
print(num_identical_pairs(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", num_identical_pairs([]))

print("Test 2 - single-element list")
print("  expected:", 0, "| got:", num_identical_pairs([5]))

print("Test 3 - two identical elements")
print("  expected:", 1, "| got:", num_identical_pairs([3,3]))

print("Test 4 - two different elements")
print("  expected:", 0, "| got:", num_identical_pairs([3,4]))


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

grade(num_identical_pairs)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 2, 3, 1, 1, 3], expected=4)   # checks the value your code returns against this example
