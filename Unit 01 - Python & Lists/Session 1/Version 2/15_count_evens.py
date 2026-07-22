def count_evens(lst):
    counter = 0
    for num in lst:
        if num % 2 == 0:
            counter += 1
    return counter

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", count_evens([]))

print("Test 2 - list containing zero (zero is even)")
print("  expected:", 1, "| got:", count_evens([0,1,3]))

print("Test 3 - negative even numbers")
print("  expected:", 2, "| got:", count_evens([-2,-4,-1]))

print("Test 4 - single even element")
print("  expected:", 1, "| got:", count_evens([8]))

print("Test 5 - single odd element")
print("  expected:", 0, "| got:", count_evens([7]))


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

grade(count_evens)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 5, 7, 9], expected=0)   # checks the value your code returns against this example
