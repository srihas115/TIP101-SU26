def find_odd_occurrences(numbers):
    pass

numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - minimal case, two singleton values")
print("  expected:", [5, 9], "| got:", find_odd_occurrences([5, 9]))

print("Test 2 - larger even counts plus an odd pair")
print("  expected:", [7, 8], "| got:", find_odd_occurrences([1,1,2,2,7,8]))

print("Test 3 - negative numbers with odd occurrence")
print("  expected:", [-1, -2], "| got:", find_odd_occurrences([3,3,-1,-2]))
