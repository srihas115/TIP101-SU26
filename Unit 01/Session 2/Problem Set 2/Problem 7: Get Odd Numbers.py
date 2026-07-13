def get_odds(nums):
    pass

nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", [], "| got:", get_odds([]))

print("Test 2 - all even numbers")
print("  expected:", [], "| got:", get_odds([2,4,6]))

print("Test 3 - negative odd numbers")
print("  expected:", [-1,-3], "| got:", get_odds([-1,-2,-3]))

print("Test 4 - list containing zero (zero is even, excluded)")
print("  expected:", [1], "| got:", get_odds([0,1]))
