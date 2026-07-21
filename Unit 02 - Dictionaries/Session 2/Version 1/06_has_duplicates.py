def has_duplicates(nums, k):
    pass

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - k greater than list length, duplicate exists somewhere")
print("  expected:", True, "| got:", has_duplicates([1,2,3,1], 100))

print("Test 2 - no duplicates at all")
print("  expected:", False, "| got:", has_duplicates([1,2,3,4], 3))

print("Test 3 - duplicate exactly at k distance (inclusive boundary)")
print("  expected:", True, "| got:", has_duplicates([1,2,3,1], 3))

print("Test 4 - duplicate just beyond k distance")
print("  expected:", False, "| got:", has_duplicates([1,2,3,4,1], 3))
