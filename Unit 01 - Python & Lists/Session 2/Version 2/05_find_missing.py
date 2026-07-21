def find_missing(nums):
    pass

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - missing number is 0")
print("  expected:", 0, "| got:", find_missing([1]))

print("Test 2 - missing number is the largest value n")
print("  expected:", 1, "| got:", find_missing([0]))

print("Test 3 - missing number is the last in a longer range")
print("  expected:", 3, "| got:", find_missing([0,1,2]))

print("Test 4 - missing number is in the middle")
print("  expected:", 2, "| got:", find_missing([3,0,1]))
