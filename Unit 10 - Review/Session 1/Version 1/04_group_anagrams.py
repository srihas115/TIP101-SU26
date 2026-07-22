'''
==============================================================================
  Unit 10: Review  ·  Session 1  ·  Version 1
  Problem 4: Group Anagrams

  Given an array of strings `strs`, group **the anagrams** together. You can
  return the answer in **any order**.

  An **Anagram** is a word or phrase formed by rearranging the letters of a
  different word or phrase, typically using all the original letters exactly
  once.

  Write your solution for `group_anagrams` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `group_anagrams` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def group_anagrams(strs):
    pass


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

grade(group_anagrams)   # ▶ Run this file to validate your solution
