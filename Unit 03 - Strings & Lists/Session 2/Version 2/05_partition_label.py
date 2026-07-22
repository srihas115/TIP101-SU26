'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 2  ·  Version 2
    Problem 5: Partition Labels

    Write a function `partition_labels()` that takes in a string `s` as a
    parameter. `s` consists of lowercase letters and represents the order of
    characters as they appear in a document. The function partitions `s` into
    as many parts as possible so that each unique letter appears in at most
    one part, and returns a list of integers representing the size of these
    parts.

    Write your solution for `partition_label` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `partition_label` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def partition_label(s):
    pass

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", [], "| got:", partition_label(""))

print("Test 2 - single character")
print("  expected:", [1], "| got:", partition_label("a"))

print("Test 3 - all-same-character string (one partition)")
print("  expected:", [4], "| got:", partition_label("aaaa"))

print("Test 4 - all unique characters (each its own partition)")
print("  expected:", [1,1,1,1], "| got:", partition_label("abcd"))


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

grade(partition_label)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('ababcbacadefegdehijhklij', expected=[9, 7, 8])   # checks the value your code returns against this example
