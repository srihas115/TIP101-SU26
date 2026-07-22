'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 3
    Problem 3: Backspace Compare

    Write a function `backspace_compare()` that takes in two strings `s` and
    `t` as parameters that both might have the backspace character `#`. The
    backspace character removes the character in front of it. The function
    returns `True` if they are equal when both are typed into empty text
    editors and `False` otherwise. Note that after backspacing an empty text,
    the text will continue empty.

    Write your solution for `backspace_compare` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `backspace_compare` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def backspace_compare(s, t):
    pass

s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - both empty strings")
print("  expected:", True, "| got:", backspace_compare("", ""))

print("Test 2 - both fully backspaced to empty")
print("  expected:", True, "| got:", backspace_compare("a#", "b#"))

print("Test 3 - backspace on empty text does nothing")
print("  expected:", True, "| got:", backspace_compare("#abc", "abc"))

print("Test 4 - trailing backspaces beyond all content")
print("  expected:", True, "| got:", backspace_compare("abc###", ""))


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

grade(backspace_compare)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('ab#c', 'ad#c', expected=True)   # checks the value your code returns against this example
