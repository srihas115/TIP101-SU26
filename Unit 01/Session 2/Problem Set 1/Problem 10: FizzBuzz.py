def fizzbuzz(n):
    pass

fizzbuzz(13)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1 (prints just 1)")
print("  expected printed output: 1")
fizzbuzz(1)

print("Test 2 - n is 3 (last value is a multiple of 3)")
print("  expected printed output: 1 / 2 / Fizz")
fizzbuzz(3)

print("Test 3 - n is 5 (last value is a multiple of 5)")
print("  expected printed output: 1 / 2 / Fizz / 4 / Buzz")
fizzbuzz(5)

print("Test 4 - n is 0 (nothing printed)")
print("  expected printed output: (nothing)")
fizzbuzz(0)
