def is_perfect_number(n):
    pass

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1 (no proper divisors sum to itself)")
print("  expected:", False, "| got:", is_perfect_number(1))

print("Test 2 - next known perfect number")
print("  expected:", True, "| got:", is_perfect_number(496))

print("Test 3 - non-perfect number")
print("  expected:", False, "| got:", is_perfect_number(10))
