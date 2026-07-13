def doubled(lst):
    pass

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [2,4,6], "| got:", doubled([1,2,3]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", doubled([]))

print("Test 3 - negative numbers")
print("  expected:", [-2,-4], "| got:", doubled([-1,-2]))

print("Test 4 - single-element list")
print("  expected:", [10], "| got:", doubled([5]))

print("Test 5 - list with zero")
print("  expected:", [0], "| got:", doubled([0]))
