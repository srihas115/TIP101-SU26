'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 3
    Problem 5: Reverse Prefix

    Write a function `reverse_prefix()` that takes in a 0-indexed string
    `word` and a character `ch` as parameters. The function reverses the
    segment of `word` that starts at index 0 and ends at the index of the
    first occurrence of `ch` (inclusive) and keeps the rest of the string the
    same. If `ch` does not exist in `word`, do nothing. Return the resulting
    string.

    Write your solution for `reverse_prefix` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `reverse_prefix` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def reverse_prefix(word, ch):
    pass

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - ch is the first character (single-char prefix, no visible change)")
print("  expected:", "abc", "| got:", reverse_prefix("abc", "a"))

print("Test 2 - ch is the last character (full reversal)")
print("  expected:", "cba", "| got:", reverse_prefix("abc", "c"))

print("Test 3 - empty word")
print("  expected:", "", "| got:", reverse_prefix("", "a"))

print("Test 4 - ch appears multiple times, uses the first occurrence")
print("  expected:", "cbaabc", "| got:", reverse_prefix("abcabc", "c"))


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

grade(reverse_prefix)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('abcdefd', 'd', expected='dcbaefd')   # checks the value your code returns against this example
