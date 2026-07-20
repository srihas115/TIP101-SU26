def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - target found (matches example)")
print("  expected:", 2, "| got:", linear_search([1,4,5,2,8], 5))

print("Test 2 - target not found")
print("  expected:", -1, "| got:", linear_search([1,4,5,2,8], 10))

print("Test 3 - empty list")
print("  expected:", -1, "| got:", linear_search([], 3))

print("Test 4 - single-element list, target present")
print("  expected:", 0, "| got:", linear_search([9], 9))

print("Test 5 - duplicate values, returns first occurrence")
print("  expected:", 1, "| got:", linear_search([5,3,3,3], 3))

print("Test 6 - target at last index")
print("  expected:", 3, "| got:", linear_search([1,2,3,4], 4))
