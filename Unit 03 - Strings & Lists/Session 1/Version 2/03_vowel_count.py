def vowel_count(s):
    pass

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", vowel_count(""))

print("Test 2 - single vowel character")
print("  expected:", 1, "| got:", vowel_count("e"))

print("Test 3 - single consonant character")
print("  expected:", 0, "| got:", vowel_count("b"))

print("Test 4 - all-same-character string, all vowels")
print("  expected:", 4, "| got:", vowel_count("aaaa"))

print("Test 5 - mixed case vowels")
print("  expected:", 5, "| got:", vowel_count("AEIOU"))

print("Test 6 - punctuation and whitespace mixed in")
print("  expected:", 3, "| got:", vowel_count("a! e? i."))


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

grade(vowel_count)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('hello world', expected=3)   # checks the value your code returns against this example
