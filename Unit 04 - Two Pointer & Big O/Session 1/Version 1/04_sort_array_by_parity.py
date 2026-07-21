def sort_array_by_parity(nums):
    pass

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: any ordering with all evens before all odds is valid, so these tests check
# the *property* (evens-before-odds, same multiset of elements) rather than one exact list.

def _is_valid_parity_sort(original, result):
    if sorted(result) != sorted(original):
        return False
    seen_odd = False
    for x in result:
        if x % 2 == 1:
            seen_odd = True
        elif seen_odd:
            return False
    return True

print("Test 1 - empty list")
result1 = sort_array_by_parity([])
print("  expected:", True, "| got:", _is_valid_parity_sort([], result1))

print("Test 2 - all evens")
original2 = [2,4,6]
result2 = sort_array_by_parity(original2)
print("  expected:", True, "| got:", _is_valid_parity_sort(original2, result2))

print("Test 3 - all odds")
original3 = [1,3,5]
result3 = sort_array_by_parity(original3)
print("  expected:", True, "| got:", _is_valid_parity_sort(original3, result3))

print("Test 4 - mixed evens and odds")
original4 = [5,2,8,1,4]
result4 = sort_array_by_parity(original4)
print("  expected:", True, "| got:", _is_valid_parity_sort(original4, result4))
