def find_missing_positive(nums):
    pass

nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-element list")
print("  expected:", 2, "| got:", find_missing_positive([1]))

print("Test 2 - missing number right after the first")
print("  expected:", 2, "| got:", find_missing_positive([1,3]))

print("Test 3 - large gap at the end")
print("  expected:", 4, "| got:", find_missing_positive([1,2,3,100]))
