def remove_element(nums, val):
    pass

nums = [5, 4, 4, 3, 4, 1]
nums_len = remove_element(nums, 4)
print(nums) # same list
print(nums_len)


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

grade(remove_element)   # ▶ Run this file to validate your solution
