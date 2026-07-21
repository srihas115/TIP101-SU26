def print_odd_indices(nums):
    pass

nums = [3,4,8,1,5,2]
print_odd_indices(nums)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_odd_indices([])

print("Test 2 - single-element list (no odd indices, nothing printed)")
print("  expected printed output: (nothing)")
print_odd_indices([9])

print("Test 3 - two-element list (only index 1 printed)")
print("  expected printed output: 20")
print_odd_indices([10, 20])

print("Test 4 - list with duplicate values")
print("  expected printed output: 5 / 5")
print_odd_indices([5,5,5,5])
