def divide_list(nums):
    pass

nums = [3,2,3,2,2,2]
print(divide_list(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - cannot be divided into pairs")
print("  expected:", False, "| got:", divide_list([1,2,3,4]))

print("Test 2 - empty list (trivially 0 pairs)")
print("  expected:", True, "| got:", divide_list([]))

print("Test 3 - all same value")
print("  expected:", True, "| got:", divide_list([5,5,5,5]))

print("Test 4 - one value has an odd count")
print("  expected:", False, "| got:", divide_list([1,1,1,2,2,2]))
