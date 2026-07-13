def count_occurrences(nums):
    pass

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", {1:1,2:2,3:3,4:1}, "| got:", count_occurrences([1,2,2,3,3,3,4]))

print("Test 2 - empty list")
print("  expected:", {}, "| got:", count_occurrences([]))

print("Test 3 - single-element list")
print("  expected:", {5:1}, "| got:", count_occurrences([5]))

print("Test 4 - negative numbers")
print("  expected:", {-1:2,-2:1}, "| got:", count_occurrences([-1,-1,-2]))

print("Test 5 - all same value")
print("  expected:", {7:4}, "| got:", count_occurrences([7,7,7,7]))
