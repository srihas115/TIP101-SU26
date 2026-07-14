def print_negatives(lst):
    for num in lst:
        if num < 0:
            print(num)

print_negatives([3,-2,2,1,-5])

print_negatives([1,2,3,4,5])

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list (nothing printed)")
print("  expected printed output: (nothing)")
print_negatives([])

print("Test 2 - single negative element")
print("  expected printed output: -4")
print_negatives([-4])

print("Test 3 - single positive element (nothing printed)")
print("  expected printed output: (nothing)")
print_negatives([7])

print("Test 4 - all negative numbers")
print("  expected printed output: -1 / -2 / -3")
print_negatives([-1,-2,-3])
