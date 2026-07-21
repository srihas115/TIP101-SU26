def group_by_frequency(lst):
    pass

lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", {}, "| got:", group_by_frequency([]))

print("Test 2 - all unique elements (all frequency 1)")
print("  expected:", {1: ['a','b','c']}, "| got:", group_by_frequency(['a','b','c']))

print("Test 3 - all elements the same")
print("  expected:", {3: ['x']}, "| got:", group_by_frequency(['x','x','x']))

print("Test 4 - single-element list")
print("  expected:", {1: ['z']}, "| got:", group_by_frequency(['z']))
