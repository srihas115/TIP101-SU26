'''
==============================================================================
    Unit 3: Strings & Lists  ·  Session 1  ·  Version 2
    Problem 4: Reverse Sentence

    Write a function `reverse_sentence()` that takes in a string `sentence` as
    a parameter and returns the string with the sentence but with the order of
    the words reversed. The sentence will only contain alphabetic characters
    and spaces to separate the words. If there is only one word in the
    sentence, the function returns the original string.

    Write your solution for `reverse_sentence` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `reverse_sentence` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


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
