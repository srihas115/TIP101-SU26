def two_sum(nums, target):
    pass

nums = [2,7,11,15,17]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - two-element list, exact sum")
print("  expected:", [0, 1], "| got:", two_sum([4, 5], 9))

print("Test 2 - negative numbers in sorted list")
print("  expected:", [0, 1], "| got:", two_sum([-4, -1], -5))

print("Test 3 - target requires the first and last elements")
print("  expected:", [0, 3], "| got:", two_sum([1, 2, 3, 9], 10))
