def find_mode(lst):
    pass

lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-element list")
print("  expected:", 9, "| got:", find_mode([9]))

print("Test 2 - tie between two values (first appeared wins)")
print("  expected:", 2, "| got:", find_mode([2,2,3,3]))

print("Test 3 - all elements the same")
print("  expected:", 6, "| got:", find_mode([6,6,6]))
