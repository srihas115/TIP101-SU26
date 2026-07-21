def find_averages_of_subarrays(k, nums):
    pass

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
print(avg_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [2.2, 2.8, 2.4, 3.6, 2.8], "| got:", find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))

print("Test 2 - k equals the length of nums (single window)")
print("  expected:", [2.0], "| got:", find_averages_of_subarrays(3, [1, 2, 3]))

print("Test 3 - k is 1 (each element is its own average)")
print("  expected:", [1.0, 2.0, 3.0], "| got:", find_averages_of_subarrays(1, [1, 2, 3]))
