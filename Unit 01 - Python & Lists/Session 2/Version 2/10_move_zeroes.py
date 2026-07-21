def move_zeroes(nums):
    pass

nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", move_zeroes([]))

print("Test 2 - all zeros (unchanged)")
print("  expected:", [0,0,0], "| got:", move_zeroes([0,0,0]))

print("Test 3 - no zeros (order preserved, unchanged)")
print("  expected:", [1,2,3], "| got:", move_zeroes([1,2,3]))

print("Test 4 - single zero")
print("  expected:", [0], "| got:", move_zeroes([0]))
