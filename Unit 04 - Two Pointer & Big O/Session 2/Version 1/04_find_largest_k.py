def find_largest_k(nums):
    pass

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no valid pair")
print("  expected:", -1, "| got:", find_largest_k([1,2,3]))

print("Test 2 - empty list")
print("  expected:", -1, "| got:", find_largest_k([]))

print("Test 3 - single pair only")
print("  expected:", 5, "| got:", find_largest_k([5,-5]))

print("Test 4 - multiple pairs, picks the largest")
print("  expected:", 3, "| got:", find_largest_k([1,-1,2,-2,3,-3]))
