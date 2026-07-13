def count_less_than(numbers, threshold):
    pass

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", 3, "| got:", count_less_than([12,8,2,4,4,10], 5))

print("Test 2 - empty list")
print("  expected:", 0, "| got:", count_less_than([], 5))

print("Test 3 - negative threshold")
print("  expected:", 2, "| got:", count_less_than([-5,-1,0,3], -1))

print("Test 4 - all elements equal to threshold (excluded, not strictly less)")
print("  expected:", 0, "| got:", count_less_than([5,5,5], 5))

print("Test 5 - all elements less than threshold")
print("  expected:", 3, "| got:", count_less_than([1,2,3], 10))
