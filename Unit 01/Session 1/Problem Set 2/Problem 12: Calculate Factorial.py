def factorial(n):
    pass

print(factorial(3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 0 (0! is 1)")
print("  expected:", 1, "| got:", factorial(0))

print("Test 2 - n is 1")
print("  expected:", 1, "| got:", factorial(1))

print("Test 3 - n is 5")
print("  expected:", 120, "| got:", factorial(5))
