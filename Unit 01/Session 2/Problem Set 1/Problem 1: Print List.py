def print_list(lst):
    pass

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_list([])

print("Test 2 - single-element list")
print("  expected printed output: pikachu")
print_list(["pikachu"])

print("Test 3 - list preserves order")
print("  expected printed output: a / b / c")
print_list(["a", "b", "c"])

print("Test 4 - list with duplicate elements")
print("  expected printed output: x / x / y")
print_list(["x", "x", "y"])
