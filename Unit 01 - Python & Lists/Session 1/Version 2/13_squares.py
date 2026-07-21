def squares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [1,4,9,16], "| got:", squares([1,2,3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", squares([]))

print("Test 3 - negative numbers")
print("  expected:", [1,4,9], "| got:", squares([-1,-2,-3]))

print("Test 4 - list containing zero")
print("  expected:", [0], "| got:", squares([0]))

print("Test 5 - single-element list")
print("  expected:", [16], "| got:", squares([4]))
