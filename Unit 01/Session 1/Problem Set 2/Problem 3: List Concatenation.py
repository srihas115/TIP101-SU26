def concatenate_list(nums):
    res = []
    res.extend(nums)
    res.extend(nums)
    return res

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [1,2,3,4,1,2,3,4], "| got:", concatenate_list([1,2,3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", concatenate_list([]))

print("Test 3 - single-element list")
print("  expected:", [7,7], "| got:", concatenate_list([7]))

print("Test 4 - list with duplicate values")
print("  expected:", [2,2,2,2], "| got:", concatenate_list([2,2]))

print("Test 5 - list with negative numbers")
print("  expected:", [-1,-2,-1,-2], "| got:", concatenate_list([-1,-2]))
