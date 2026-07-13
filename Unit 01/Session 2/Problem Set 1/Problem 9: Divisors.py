def find_divisors(n):
    pass

lst = find_divisors(6)
print(lst)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", [1,2,3,6], "| got:", find_divisors(6))

print("Test 2 - n is 1 (only divisor is itself)")
print("  expected:", [1], "| got:", find_divisors(1))

print("Test 3 - n is prime")
print("  expected:", [1,7], "| got:", find_divisors(7))

print("Test 4 - n has many divisors")
print("  expected:", [1,2,3,4,6,12], "| got:", find_divisors(12))
