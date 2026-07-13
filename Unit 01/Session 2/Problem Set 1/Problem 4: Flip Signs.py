def flip_sign(lst):
    pass

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [-1, 2, 3, -4], "| got:", flip_sign([1,-2,-3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", flip_sign([]))

print("Test 3 - all positive numbers")
print("  expected:", [-1,-2,-3], "| got:", flip_sign([1,2,3]))

print("Test 4 - all negative numbers")
print("  expected:", [1,2,3], "| got:", flip_sign([-1,-2,-3]))

print("Test 5 - list containing zero (sign flip has no effect on zero)")
print("  expected:", [0, -5], "| got:", flip_sign([0, 5]))
