'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 1
    Problem 1: Hello World!

    Given the following lines of code, work with your group members to place
    the lines in order and write and call your first Python function!

    a. `print("Hello world!")` b. `def hello_world():` c. `hello_world()`

    Write your solution for `hello_world` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `hello_world` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def hello_world():
    print("Hello world!")


# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - basic call")
print("  expected printed output: Hello world!")
hello_world()

print("Test 2 - calling twice in a row still prints each time")
print("  expected printed output (two lines): Hello world! / Hello world!")
hello_world()
hello_world()


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

grade(hello_world)   # ▶ Run this file to validate your solution
