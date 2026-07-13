def two_sum(nums, target):
    pass

nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - two-element list, exact match")
print("  expected:", [0, 1], "| got:", two_sum([4, 5], 9))

print("Test 2 - negative numbers")
print("  expected:", [0, 1], "| got:", two_sum([-3, -1], -4))

print("Test 3 - target requires the last two elements")
print("  expected:", [2, 3], "| got:", two_sum([1, 2, 3, 4], 7))
