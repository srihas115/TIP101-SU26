def binary_substrings_count(s):
    pass

s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", binary_substrings_count(""))

print("Test 2 - single character")
print("  expected:", 0, "| got:", binary_substrings_count("0"))

print("Test 3 - minimal valid substring '01'")
print("  expected:", 1, "| got:", binary_substrings_count("01"))

print("Test 4 - minimal valid substring '10'")
print("  expected:", 1, "| got:", binary_substrings_count("10"))
