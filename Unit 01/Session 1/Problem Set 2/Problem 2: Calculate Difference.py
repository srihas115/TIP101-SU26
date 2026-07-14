def difference(a, b):
    return a-b

diff = difference(8, 3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - a=8, b=3 (matches example)")
print("  expected:", 5, "| got:", difference(8, 3))

print("Test 2 - b greater than a (negative result)")
print("  expected:", -5, "| got:", difference(3, 8))

print("Test 3 - a equals b (zero result)")
print("  expected:", 0, "| got:", difference(4, 4))

print("Test 4 - both zero")
print("  expected:", 0, "| got:", difference(0, 0))

print("Test 5 - negative numbers")
print("  expected:", -3, "| got:", difference(-5, -2))
