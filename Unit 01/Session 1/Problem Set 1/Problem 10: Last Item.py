def get_last(lst):
    if len(lst) == 0:
        return None
    return lst[len(lst) - 1]

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", None, "| got:", get_last([]))

print("Test 2 - single-element list")
print("  expected:", 9, "| got:", get_last([9]))

print("Test 3 - unsorted list")
print("  expected:", 2, "| got:", get_last([4,1,3,2]))

print("Test 4 - list with negative numbers")
print("  expected:", -3, "| got:", get_last([-7,-1,-3]))

print("Test 5 - already-sorted list")
print("  expected:", 4, "| got:", get_last([1,2,3,4]))
