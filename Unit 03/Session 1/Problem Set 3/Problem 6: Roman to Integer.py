def roman_to_int(s):
    pass

s = "XL"
print(roman_to_int(s))

s2 = "LVIII"
print(roman_to_int(s2))

s3 = "MCMXCIV"
print(roman_to_int(s3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single character")
print("  expected:", 1, "| got:", roman_to_int("I"))

print("Test 2 - subtractive pair (IV)")
print("  expected:", 4, "| got:", roman_to_int("IV"))

print("Test 3 - subtractive pair (IX)")
print("  expected:", 9, "| got:", roman_to_int("IX"))

print("Test 4 - repeated same symbol, no subtraction")
print("  expected:", 3, "| got:", roman_to_int("III"))

print("Test 5 - larger mixed numeral")
print("  expected:", 2024, "| got:", roman_to_int("MMXXIV"))
