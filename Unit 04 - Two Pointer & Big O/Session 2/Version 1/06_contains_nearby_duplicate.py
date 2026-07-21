def contains_nearby_duplicate(lst, k):
    pass

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - k greater than list length, duplicate exists somewhere")
print("  expected:", True, "| got:", contains_nearby_duplicate([1,2,3,1], 100))

print("Test 2 - no duplicates at all")
print("  expected:", False, "| got:", contains_nearby_duplicate([1,2,3,4], 3))

print("Test 3 - duplicate exactly at k distance (boundary)")
print("  expected:", True, "| got:", contains_nearby_duplicate([1,2,3,1], 3))

print("Test 4 - empty list")
print("  expected:", False, "| got:", contains_nearby_duplicate([], 2))
