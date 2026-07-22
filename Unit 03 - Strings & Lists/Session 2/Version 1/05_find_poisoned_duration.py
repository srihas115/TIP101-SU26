'''
==============================================================================
  Unit 3: Strings & Lists  ·  Session 2  ·  Version 1
  Problem 5: Teemo's Attack

  In the game **League of Legends**, Teemo attacks his enemy Ashe with
  poison arrows. Write a function `find_poisoned_duration()` that takes in
  two parameters: `time_series` (*the time at which Teemo's attacks hits
  Ashe*) and `time_duration` (*the duration of the poisoning effect*). The
  function returns the total time that Ashe is in a poisoned condition.

  `time_series` is a list of integers that represents the times at which
  Teemo attacks and makes Ashe poisoned for the exact `time_duration`.

  If Teemo hits Ashe while she is still poisoned, the poison's duration
  starts over. For example, if Teemo attacks at times `1` and `4` for 3
  seconds, the states at each time would be:

  Write your solution for `find_poisoned_duration` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `find_poisoned_duration` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def find_poisoned_duration(time_series, duration):
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

grade(find_poisoned_duration)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 4, 9], 3, expected=8)   # checks the value your code returns against this example
