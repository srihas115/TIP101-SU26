def count_pairs(nums, target):
    pass

nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", count_pairs([], 2))

print("Test 2 - single-element list (no pairs possible)")
print("  expected:", 0, "| got:", count_pairs([5], 2))

print("Test 3 - two-element list, pair qualifies")
print("  expected:", 1, "| got:", count_pairs([1,1], 3))

print("Test 4 - two-element list, pair does not qualify")
print("  expected:", 0, "| got:", count_pairs([5,5], 3))
