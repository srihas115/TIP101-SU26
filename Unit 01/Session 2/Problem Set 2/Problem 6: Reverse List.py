def reverse_list(lst):
    pass

lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", reverse_list([]))

print("Test 2 - single-element list")
print("  expected:", [9], "| got:", reverse_list([9]))

print("Test 3 - list with duplicate values")
print("  expected:", [2,2,1], "| got:", reverse_list([1,2,2]))

print("Test 4 - negative numbers")
print("  expected:", [-3,-2,-1], "| got:", reverse_list([-1,-2,-3]))
