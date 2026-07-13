def count_evens(lst):
    pass

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", count_evens([]))

print("Test 2 - list containing zero (zero is even)")
print("  expected:", 1, "| got:", count_evens([0,1,3]))

print("Test 3 - negative even numbers")
print("  expected:", 2, "| got:", count_evens([-2,-4,-1]))

print("Test 4 - single even element")
print("  expected:", 1, "| got:", count_evens([8]))

print("Test 5 - single odd element")
print("  expected:", 0, "| got:", count_evens([7]))
