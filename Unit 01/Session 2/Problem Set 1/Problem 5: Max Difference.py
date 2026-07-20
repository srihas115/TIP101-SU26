def max_difference(lst):
    if len(lst) == 0 or len(lst) == 1:
        return 0
    
    min = lst[0]
    max = lst[0]
    
    for num in lst:
        if num > max:
            max = num
        if num < min:
            min = num
    
    return max - min
    

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", 20, "| got:", max_difference([5,22,8,10,2]))

print("Test 2 - single-element list (no difference)")
print("  expected:", 0, "| got:", max_difference([7]))

print("Test 3 - negative numbers")
print("  expected:", 9, "| got:", max_difference([-5,-1,-10]))

print("Test 4 - all elements equal")
print("  expected:", 0, "| got:", max_difference([4,4,4]))

print("Test 5 - already-sorted ascending list")
print("  expected:", 4, "| got:", max_difference([1,2,3,4,5]))
