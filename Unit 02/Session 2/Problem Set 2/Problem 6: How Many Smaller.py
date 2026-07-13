def smaller_numbers_than_current(nums):
    pass

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", smaller_numbers_than_current([]))

print("Test 2 - all elements equal")
print("  expected:", [0,0,0], "| got:", smaller_numbers_than_current([5,5,5]))

print("Test 3 - single-element list")
print("  expected:", [0], "| got:", smaller_numbers_than_current([7]))

print("Test 4 - already-sorted ascending list")
print("  expected:", [0,1,2,3], "| got:", smaller_numbers_than_current([1,2,3,4]))
