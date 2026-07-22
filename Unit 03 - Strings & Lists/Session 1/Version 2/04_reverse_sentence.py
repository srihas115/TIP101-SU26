def reverse_sentence(sentence):
    pass

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", "good no to up am I swear solemnly I", "| got:", reverse_sentence("I solemnly swear I am up to no good"))

print("Test 2 - single word (unchanged)")
print("  expected:", "hello", "| got:", reverse_sentence("hello"))

print("Test 3 - empty string")
print("  expected:", "", "| got:", reverse_sentence(""))

print("Test 4 - two words")
print("  expected:", "world hello", "| got:", reverse_sentence("hello world"))


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

grade(reverse_sentence)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('I solemnly swear I am up to no good', expected='good no to up am I swear solemnly I')   # checks the value your code returns against this example
