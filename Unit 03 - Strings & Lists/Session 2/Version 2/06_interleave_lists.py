def interleave_lists(lst1, lst2):
    pass

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - both lists empty")
print("  expected:", [], "| got:", interleave_lists([], []))

print("Test 2 - one list empty")
print("  expected:", [1,2,3], "| got:", interleave_lists([1,2,3], []))

print("Test 3 - equal-length lists")
print("  expected:", [1,10,2,20], "| got:", interleave_lists([1,2], [10,20]))

print("Test 4 - second list longer than the first")
print("  expected:", [1,10,20,30], "| got:", interleave_lists([1], [10,20,30]))
