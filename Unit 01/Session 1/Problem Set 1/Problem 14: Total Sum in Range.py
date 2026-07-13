def sum_range(start, stop):
    pass

sum = sum_range(3, 9)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - start=3, stop=9 (matches example)")
print("  expected:", 42, "| got:", sum_range(3,9))

print("Test 2 - start equals stop (single number range)")
print("  expected:", 5, "| got:", sum_range(5,5))

print("Test 3 - start greater than stop (empty range)")
print("  expected:", 0, "| got:", sum_range(9,3))

print("Test 4 - negative range")
print("  expected:", -6, "| got:", sum_range(-3,-1))
