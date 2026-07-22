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
    pass

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty time_series")
print("  expected:", 0, "| got:", find_poisoned_duration([], 3))

print("Test 2 - single attack")
print("  expected:", 3, "| got:", find_poisoned_duration([5], 3))

print("Test 3 - non-overlapping attacks (no reset needed)")
print("  expected:", 6, "| got:", find_poisoned_duration([1, 10], 3))

print("Test 4 - overlapping attacks, matches the walkthrough in the spec")
print("  expected:", 5, "| got:", find_poisoned_duration([1, 4], 3))


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
