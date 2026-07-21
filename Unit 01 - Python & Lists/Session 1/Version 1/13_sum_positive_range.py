def sum_positive_range(stop):
    sum = 0
    for i in range(stop+1):
        sum += i
    return sum

sum = sum_positive_range(6)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - stop is 6 (matches example)")
print("  expected:", 21, "| got:", sum_positive_range(6))

print("Test 2 - stop is 1")
print("  expected:", 1, "| got:", sum_positive_range(1))

print("Test 3 - stop is 0 (no positive numbers to sum)")
print("  expected:", 0, "| got:", sum_positive_range(0))

print("Test 4 - negative stop (no positive numbers to sum)")
print("  expected:", 0, "| got:", sum_positive_range(-5))
