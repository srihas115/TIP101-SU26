'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 1
    Problem 8: Multiples of Five

    Write a function `multiples_of_five()` that prints out multiples of 5
    between 1 and 100 (inclusive).

    Write your solution for `multiples_of_five` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `multiples_of_five` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def multiples_of_five():
    for i in range(5, 105, 5):
        print(i)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - basic call")
print("  expected printed output: 5, 10, 15, ..., 95, 100 (20 lines, first is 5, last is 100)")
multiples_of_five()

print("Test 2 - calling again produces the same output")
print("  expected printed output: same 20 lines again")
multiples_of_five()


'''
==============================================================================
    PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(multiples_of_five)   # ▶ Run this file to validate your solution
