def counter(stop):
    pass

counter(7)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - stop is 1 (prints just 1)")
print("  expected printed output: 1")
counter(1)

print("Test 2 - stop is 0 (no numbers printed)")
print("  expected printed output: (nothing)")
counter(0)

print("Test 3 - negative stop (no numbers printed)")
print("  expected printed output: (nothing)")
counter(-5)

print("Test 4 - stop is 3")
print("  expected printed output: 1 / 2 / 3")
counter(3)
