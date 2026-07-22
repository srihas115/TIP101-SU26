'''
==============================================================================
  Unit 2: Dictionaries  ·  Session 1  ·  Version 2
  Problem 7: Best Movie Genre

  Imagine you're contributing to a move recommendation engine, and you're
  tasked with writing a function named `most_popular_genre()` that returns
  the genre with the highest average rating across all movies.

  The function takes in a list of dictionaries named `movies` as a
  parameter. Each dictionary represents data associated with a movie,
  including its title, genre, and rating. The function calculates the
  average rating for each genre and returns the genre with the highest
  average rating.

  Write your solution for `most_popular_genre` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `most_popular_genre` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def most_popular_genre(movies):
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

grade(most_popular_genre)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([{'title': 'Inception', 'genre': 'Science Fiction', 'rating': 8.8}, {'title': 'The Matrix', 'genre': 'Science Fiction', 'rating': 8.7}, {'title': 'Pride and Prejudice', 'genre': 'Romance', 'rating': 7.8}, {'title': 'Sense and Sensibility', 'genre': 'Romance', 'rating': 7.7}], expected='Science Fiction')   # checks the value your code returns against this example
