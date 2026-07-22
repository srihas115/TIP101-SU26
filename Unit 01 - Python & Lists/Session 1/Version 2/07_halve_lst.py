def halve_lst(lst):
    result = []
    for number in lst:
        halved = number/2
        # result.append(halved)
        result.append(int(halved)) # should be int(halved))
    return result

print(halve_lst([2,4,6,8]))


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

grade(halve_lst)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([2, 4, 6, 8], expected=[1.0, 2.0, 3.0, 4.0])   # checks the value your code returns against this example
