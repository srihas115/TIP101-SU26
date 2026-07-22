def update_or_warn(records, item, update_value):
    pass

records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
# Print the input dictionary after running the function to check if it was modified
print(records)
update_or_warn(records, "banana", 5)
print(records)


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

grade(update_or_warn)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test({'apple': 1, 'banana': 2, 'orange': 3}, 'grape', 4, expected={'apple': 1, 'banana': 2, 'orange': 3})   # checks the updated first argument against this example
