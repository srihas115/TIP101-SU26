def min_distance(words, word1, word2):
    pass

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - words are adjacent, distance of 1")
print("  expected:", 1, "| got:", min_distance(["a", "b"], "a", "b"))

print("Test 2 - multiple occurrences, closest pair should be chosen")
print("  expected:", 1, "| got:", min_distance(["a", "c", "b", "a"], "a", "b"))

print("Test 3 - two-element list with the same word twice is same word, treat as adjacent")
print("  expected:", 1, "| got:", min_distance(["a", "a"], "a", "a"))

print("Test 4 - words separated by several other words")
print("  expected:", 4, "| got:", min_distance(['a', 'x', 'y', 'z', 'b'], 'a', 'b'))

print("Test 5 - order of word1/word2 swapped gives same distance")
print("  expected:", 3, "| got:", min_distance(['the', 'quick', 'brown', 'fox', 'jumped', 'the'], 'jumped', 'quick'))


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

grade(min_distance)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(['the', 'quick', 'brown', 'fox', 'jumped', 'the'], 'quick', 'jumped', expected=3)   # checks the value your code returns against this example
