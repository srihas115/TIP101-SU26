'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 3
    Problem 3: Evaluate Two Sum
==============================================================================
'''


def two_sum(nums, target):
    prev_map = {}  # Value to index mapping

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i
