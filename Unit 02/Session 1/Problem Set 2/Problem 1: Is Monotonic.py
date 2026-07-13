def is_monotonic(nums):
    pass

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (vacuously monotonic)")
print("  expected:", True, "| got:", is_monotonic([]))

print("Test 2 - single element list")
print("  expected:", True, "| got:", is_monotonic([5]))

print("Test 3 - all equal elements")
print("  expected:", True, "| got:", is_monotonic([4, 4, 4, 4]))

print("Test 4 - strictly increasing")
print("  expected:", True, "| got:", is_monotonic([1, 2, 3, 4]))

print("Test 5 - strictly decreasing")
print("  expected:", True, "| got:", is_monotonic([9, 7, 5, 1]))

print("Test 6 - non-monotonic with a dip then rise")
print("  expected:", False, "| got:", is_monotonic([1, 5, 2, 8]))
