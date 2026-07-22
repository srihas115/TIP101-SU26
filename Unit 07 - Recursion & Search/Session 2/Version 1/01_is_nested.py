'''

3. plan
    ((())) --> empty
    (

    

'''

def is_nested(s):
    if s == "":
        return True
    if s[0] == "(" and s[-1] == ")":
        return is_nested(s[1:-1])
    return False

# Example Input: "(())"
example = "(())"
print(is_nested(example))


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

grade(is_nested)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('(())', expected=True)   # checks the value your code returns against this example
