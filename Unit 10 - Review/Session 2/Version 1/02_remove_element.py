'''
==============================================================================
    Unit 10: Review  ·  Session 2  ·  Version 1
    Problem 2: Remove Element

    Given a list of integers `nums` and an integer `val`, remove all
    occurrences of `val` in `nums` **[in-
    place](https://en.wikipedia.org/wiki/In-place_algorithm)**. The order of
    the elements may be changed. Then return *the number of elements in*
    `nums` *which are not equal to* `val`.

    Consider the number of elements in `nums` which are not equal to `val` be
    `k`, for your response to be acceptable, you need to do the following
    things:

    - Change the list `nums` such that the first `k` elements of `nums`
    contain the elements which are not equal to `val`. The remaining elements
    of `nums` are not important as well as the size of `nums`. - Return `k`

    Write your solution for `remove_element` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `remove_element` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 
    input: we are given a list of nums and a target value
    output: number of elements in nums that are NOT equal to val
    core logic: 
    
Match:
    list traversal / manipulation
    
Plan:
    for loop through the list of nums by index in reverse
        if the current number matches the target value
            remove nums at index
    
    return the size of the list

'''


def remove_element(nums, val):
    for index in range(len(nums)-1, -1, -1):
        if nums[index] == val:
            nums.pop(index)
    
    return len(nums)

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
