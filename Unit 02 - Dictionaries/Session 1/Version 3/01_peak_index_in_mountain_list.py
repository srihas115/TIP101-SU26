def peak_index_in_mountain_list(lst):
    pass

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - minimal 3-element mountain")
print("  expected:", 1, "| got:", peak_index_in_mountain_list([1,3,1]))

print("Test 2 - peak near the start")
print("  expected:", 1, "| got:", peak_index_in_mountain_list([1,10,2,1]))

print("Test 3 - peak near the end")
print("  expected:", 3, "| got:", peak_index_in_mountain_list([1,2,3,10,5]))

print("Test 4 - negative numbers")
print("  expected:", 2, "| got:", peak_index_in_mountain_list([-5,-1,0,-2,-10]))
