'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 1
  Problem 7: Best Book

  Imagine you are working on a book review software like
  [Goodreads](https://www.goodreads.com/). Write a function named
  `highest_rated()` that returns the book with the highest rating.

  The function should take in a **list of dictionaries** named `books` as a
  parameter. Each dictionary represents data associated with a book,
  including its title, author, and rating. The function should return the
  dictionary for the book with the highest rating.

  Write your solution for `highest_rated` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `highest_rated` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def highest_rated(books):
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

grade(highest_rated)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([{'title': 'T1', 'author': 'Zevin', 'rating': 4.18}, {'title': 'T2', 'author': 'Abdurraqib', 'rating': 4.47}, {'title': 'T3', 'author': 'Reid', 'rating': 4.4}], expected={'title': 'T2', 'author': 'Abdurraqib', 'rating': 4.47})   # checks the value your code returns against this example
