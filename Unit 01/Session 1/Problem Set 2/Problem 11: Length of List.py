def list_length(lst):
    pass

lst = [2,4,6,8,10]
length = list_length(lst)
print(length)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", list_length([]))

print("Test 2 - single-element list")
print("  expected:", 1, "| got:", list_length([9]))

print("Test 3 - list with duplicate values")
print("  expected:", 4, "| got:", list_length([2,2,2,2]))

print("Test 4 - larger list")
print("  expected:", 6, "| got:", list_length([1,2,3,4,5,6]))
