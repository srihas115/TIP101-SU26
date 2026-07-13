def power(base, exponent):
    pass

pow1 = power(2,5)
print(pow1)
pow2 = power(3,3)
print(pow2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - exponent is 0")
print("  expected:", 1, "| got:", power(5, 0))

print("Test 2 - base is 0, positive exponent")
print("  expected:", 0, "| got:", power(0, 3))

print("Test 3 - negative base, even exponent")
print("  expected:", 25, "| got:", power(-5, 2))

print("Test 4 - base is 1")
print("  expected:", 1, "| got:", power(1, 10))

print("Test 5 - exponent is 1")
print("  expected:", 7, "| got:", power(7, 1))
