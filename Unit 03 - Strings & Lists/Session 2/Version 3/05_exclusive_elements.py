def exclusive_elements(lst1, lst2):
    pass

lst1 = [3,1,8,10]
lst2 = [4,5,3,7,8]
excl_lst = exclusive_elements(lst1, lst2)
print(excl_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty lists")
print("  expected:", [], "| got:", exclusive_elements([], []))

print("Test 2 - identical lists (nothing exclusive)")
print("  expected:", [], "| got:", exclusive_elements([1,2], [1,2]))

print("Test 3 - completely disjoint lists")
print("  expected:", [1,2,3,4], "| got:", exclusive_elements([1,2], [3,4]))

print("Test 4 - one list empty")
print("  expected:", [5,6], "| got:", exclusive_elements([5,6], []))
