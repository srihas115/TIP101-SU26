'''
==============================================================================
    Unit 2: Dictionaries  ·  Session 2  ·  Version 1
    Problem 1: Cast Vote

    Write a function `cast_vote()` that records a vote for a candidate in an
    election. The function accepts a dictionary `votes` that maps candidates
    to their current number of votes and a string `candidate` that represents
    the candidate the user would like to vote for. If the candidate doesn't
    exist, add them to the dictionary. The function should return the updated
    dictionary.

    Write your solution for `cast_vote` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `cast_vote` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def cast_vote(votes, candidate):
    pass

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)


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

grade(cast_vote)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'Alice': 5, 'Bob': 3}, 'Alice', expected={'Alice': 6, 'Bob': 3})   # checks the value your code returns against this example
