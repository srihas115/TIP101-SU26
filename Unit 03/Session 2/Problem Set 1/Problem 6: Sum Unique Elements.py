def sum_of_unique_elements(lst1, lst2):
    pass

lstA = [1, 2 ,3, 4]
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty lst1")
print("  expected:", 0, "| got:", sum_of_unique_elements([], [1,2,3]))

print("Test 2 - lst2 empty (only the appears-once condition matters)")
print("  expected:", 6, "| got:", sum_of_unique_elements([1,2,3], []))

print("Test 3 - element appears twice in lst1 (excluded, not unique)")
print("  expected:", 3, "| got:", sum_of_unique_elements([3,5,5], []))

print("Test 4 - all elements of lst1 also appear in lst2 (all excluded)")
print("  expected:", 0, "| got:", sum_of_unique_elements([1,2], [1,2]))
