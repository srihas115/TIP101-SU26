def count_negatives(k, nums):
    pass

lst = [-1, 2, -2, 3, 5, -7, -5]
print(count_negatives(lst, 3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: calls follow the same (list, k) argument order as the example call above.

print("Test 1 - k equals the length of the list (single window)")
print("  expected:", [2], "| got:", count_negatives([-1,-2,3], 3))

print("Test 2 - no negatives at all")
print("  expected:", [0,0,0], "| got:", count_negatives([1,2,3,4], 2))

print("Test 3 - all negative")
print("  expected:", [2,2], "| got:", count_negatives([-1,-2,-3], 2))
