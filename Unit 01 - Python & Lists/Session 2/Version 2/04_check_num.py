def check_num(lst, num):
    pass

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", False, "| got:", check_num([], 5))

print("Test 2 - num present at first index")
print("  expected:", True, "| got:", check_num([5,2,3], 5))

print("Test 3 - num present at last index")
print("  expected:", True, "| got:", check_num([5,2,3], 3))

print("Test 4 - negative number present")
print("  expected:", True, "| got:", check_num([-5,-2,3], -5))
