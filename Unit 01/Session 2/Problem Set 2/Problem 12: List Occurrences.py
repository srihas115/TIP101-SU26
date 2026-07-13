def find_all_occurrences(lst, target):
    pass

lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - target not present")
print("  expected:", [], "| got:", find_all_occurrences([1,2,3], 9))

print("Test 2 - empty list")
print("  expected:", [], "| got:", find_all_occurrences([], 2))

print("Test 3 - target appears once")
print("  expected:", [2], "| got:", find_all_occurrences([5,6,2,8], 2))

print("Test 4 - target appears at every index")
print("  expected:", [0,1,2], "| got:", find_all_occurrences([7,7,7], 7))
