def doubled(lst):
    for item in lst:
        print(int(item * 2))
        
lst = [1,2,3]
print(doubled(lst))

print()

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
doubled([])

print("Test 2 - negative numbers")
print("  expected printed output: -2 / -4")
doubled([-1, -2])

print("Test 3 - single-element list")
print("  expected printed output: 10")
doubled([5])

print("Test 4 - list containing zero")
print("  expected printed output: 0 / 6")
doubled([0, 3])
