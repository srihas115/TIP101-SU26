def get_evens(lst):
    evens_lst = []
    for num in lst:
        if num % 2 == 0:
            evens_lst.append(num)
    return evens_lst

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [2, 4], "| got:", get_evens([1,2,3,4]))

print("Test 2 - empty list")
print("  expected:", [], "| got:", get_evens([]))

print("Test 3 - all odd numbers")
print("  expected:", [], "| got:", get_evens([1,3,5]))

print("Test 4 - negative even numbers")
print("  expected:", [-2, -4], "| got:", get_evens([-2,-3,-4]))

print("Test 5 - list containing zero (zero is even)")
print("  expected:", [0], "| got:", get_evens([0, 1]))
