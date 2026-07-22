'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 1
    Problem 7: What time is it?

    **Let's put what we learned in Problems 1-4 all together!** Write a
    function named `what_time_is_it()` that takes an integer `hour` as a
    parameter. If `hour` is 2, the function should return `"taco time 🌮"`. If
    `hour` is 12, the function should return `"peanut butter jelly time 🥪”`.
    Otherwise, the function should return `"nap time 😴"`.

    Example Usage:

    Write your solution for `what_time_is_it` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `what_time_is_it` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - hour is 2 (taco time)")
print("  expected:", "taco time 🌮", "| got:", what_time_is_it(2))

print("Test 2 - hour is 12 (peanut butter jelly time)")
print("  expected:", "peanut butter jelly time 🥪", "| got:", what_time_is_it(12))

print("Test 3 - hour is 0 (nap time)")
print("  expected:", "nap time 😴", "| got:", what_time_is_it(0))

print("Test 4 - negative hour (nap time)")
print("  expected:", "nap time 😴", "| got:", what_time_is_it(-3))

print("Test 5 - large hour value (nap time)")
print("  expected:", "nap time 😴", "| got:", what_time_is_it(100))


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

grade(what_time_is_it)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(2, expected='taco time 🌮')   # checks the value your code returns against this example
