def above_threshold(lst, threshold):
    pass

lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", above_threshold([], 5))

print("Test 2 - single-element list above threshold")
print("  expected:", [7], "| got:", above_threshold([7], 5))

print("Test 3 - single-element list equal to threshold (excluded, not > threshold)")
print("  expected:", [], "| got:", above_threshold([5], 5))

print("Test 4 - negative numbers with negative threshold")
print("  expected:", [-1, -5], "| got:", above_threshold([-1,-5,-10], -6))

print("Test 5 - unsorted list, order preserved")
print("  expected:", [9, 8], "| got:", above_threshold([1,9,3,8,2], 4))
