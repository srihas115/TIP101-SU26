def find_intersection(lst1, lst2):
    pass

lst1 = [1,2,4,6,7]
lst2 = [2,3,4,7]
print(find_intersection(lst1, lst2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty lists")
print("  expected:", [], "| got:", find_intersection([], []))

print("Test 2 - no overlap")
print("  expected:", [], "| got:", find_intersection([1,2], [3,4]))

print("Test 3 - identical lists")
print("  expected:", [1,2,3], "| got:", find_intersection([1,2,3], [1,2,3]))

print("Test 4 - partial overlap")
print("  expected:", [3,7], "| got:", find_intersection([1,3,5,7], [3,7,9]))
