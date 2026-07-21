def find_min_index_of_repeating(nums):
    pass

nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", None, "| got:", find_min_index_of_repeating([]))

print("Test 2 - single-element list")
print("  expected:", None, "| got:", find_min_index_of_repeating([7]))

print("Test 3 - duplicate at the very start")
print("  expected:", 0, "| got:", find_min_index_of_repeating([1,1,2,3]))

print("Test 4 - all unique elements")
print("  expected:", None, "| got:", find_min_index_of_repeating([1,2,3,4]))
