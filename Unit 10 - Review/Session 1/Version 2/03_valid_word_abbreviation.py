'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 2
  Problem 3: Valid Word Abbreviation

  A string can be **abbreviated** by replacing any number of **non-
  adjacent**, **non-empty** substrings with their lengths. The lengths
  **should not** have leading zeros.

  For example, a string such as `"substitution"` could be abbreviated as
  (but not limited to):

  - `"s10n"` (`"s ubstitutio n"`) - `"sub4u4"` (`"sub stit u tion"`) -
  `"12"` (`"substitution"`) - `"su3i1u2on"` (`"su bst i t u ti on"`) -
  `"substitution"` (no substrings replaced)

  The following are **not valid** abbreviations:

  - `"s55n"` (`"s ubsti tutio n"`, the replaced substrings are adjacent) -
  `"s010n"` (has leading zeros) - `"s0ubstitution"` (replaces an empty
  substring)

  Given a string `word` and an abbreviation `abbr`, return `True` if *the
  string **matches** the given abbreviation*. Return `False` otherwise.

  A **substring** is a contiguous **non-empty** sequence of characters
  within a string.

  Write your solution for `valid_word_abbreviation` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `valid_word_abbreviation` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def valid_word_abbreviation(word, abbr):
    pass  # replace this line with your solution













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

grade(valid_word_abbreviation)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('internationalization', 'i12iz4n', expected=True)   # checks the value your code returns against this example
