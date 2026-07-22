'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 3
  Problem 5: Average Book Ratings

  Write a function `average_book_ratings()`, that calculates the average
  rating for each book in a collection. The function takes one parameter: a
  dictionary `book_ratings` where each key-value pair represents a book
  title and a list of its ratings, respectively. Ratings are represented as
  floating-point numbers. The function should return a new dictionary with
  book titles as keys and their average rating.

  Write your solution for `average_book_ratings` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `average_book_ratings` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def average_book_ratings(book_ratings):
    pass

book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}


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

grade(average_book_ratings)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'The Great Gatsby': [4.5, 3.0, 5.0], 'To Kill a Mockingbird': [4.8, 5.0, 4.0, 4.9]}, expected={'The Great Gatsby': 4.166666666666667, 'To Kill a Mockingbird': 4.675})   # checks the value your code returns against this example
