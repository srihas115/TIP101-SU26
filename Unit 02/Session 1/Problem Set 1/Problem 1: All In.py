def all_in(a, b):
    pass

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list a (vacuously true)")
print("  expected:", True, "| got:", all_in([], [1, 2, 3]))

print("Test 2 - empty list b, non-empty a")
print("  expected:", False, "| got:", all_in([1], []))

print("Test 3 - both lists empty")
print("  expected:", True, "| got:", all_in([], []))

print("Test 4 - duplicates in a, all present in b")
print("  expected:", True, "| got:", all_in([1, 1, 2], [1, 2, 3]))

print("Test 5 - a has an element not in b")
print("  expected:", False, "| got:", all_in([1, 4], [1, 2, 3]))

print("Test 6 - identical lists")
print("  expected:", True, "| got:", all_in([1, 2, 3], [1, 2, 3]))
