def is_prime(n):
    pass

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1 (not prime by definition)")
print("  expected:", False, "| got:", is_prime(1))

print("Test 2 - n is 2 (smallest prime)")
print("  expected:", True, "| got:", is_prime(2))

print("Test 3 - n is 0")
print("  expected:", False, "| got:", is_prime(0))

print("Test 4 - larger prime")
print("  expected:", True, "| got:", is_prime(17))
