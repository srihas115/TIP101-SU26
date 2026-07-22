'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 2  ·  Version 2
    Problem 10: Move Zeroes

    Write a function `move_zeroes()` that takes in an integer list `nums` and
    returns a new list with all the 0 values moved to the end of the list. The
    relative non-zero elements in the original list should be maintained.

    Write your solution for `move_zeroes` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `move_zeroes` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''

# Time: O(n)
# Space: O(n)
def move_zeroes1(nums):
    new_nums = []
    count_zeros = 0
    for num in nums:
        if num == 0:
            count_zeros += 1
        else:
            new_nums.append(num)
    
    for i in range(count_zeros):
        new_nums.append(0)
        
    return new_nums

# Time: O(n)
# Space: O(1), because we use the two-pointer approach
def move_zeroes(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[insert_pos] = nums[insert_pos], nums[i]
            insert_pos += 1
    return nums

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", move_zeroes([]))

print("Test 2 - all zeros (unchanged)")
print("  expected:", [0,0,0], "| got:", move_zeroes([0,0,0]))

print("Test 3 - no zeros (order preserved, unchanged)")
print("  expected:", [1,2,3], "| got:", move_zeroes([1,2,3]))

print("Test 4 - single zero")
print("  expected:", [0], "| got:", move_zeroes([0]))


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

grade(move_zeroes)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([1, 0, 2, 3, 0, 0, 4], expected=[1, 2, 3, 4, 0, 0, 0])   # checks the value your code returns against this example
