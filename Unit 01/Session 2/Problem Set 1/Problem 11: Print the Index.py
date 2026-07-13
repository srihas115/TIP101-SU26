def print_indices(lst):
    pass

lst = [5,1,3,8,2]
print_indices(lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_indices([])

print("Test 2 - single-element list")
print("  expected printed output: 0")
print_indices(["a"])

print("Test 3 - three-element list")
print("  expected printed output: 0 / 1 / 2")
print_indices(["a", "b", "c"])
