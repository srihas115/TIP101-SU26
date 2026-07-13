def list_to_number(digits):
    pass

digits = [1,0,3]
number = list_to_number(digits)
print(number)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single digit")
print("  expected:", 7, "| got:", list_to_number([7]))

print("Test 2 - leading zero digit")
print("  expected:", 5, "| got:", list_to_number([0,5]))

print("Test 3 - all same digit")
print("  expected:", 999, "| got:", list_to_number([9,9,9]))

print("Test 4 - single zero digit")
print("  expected:", 0, "| got:", list_to_number([0]))
