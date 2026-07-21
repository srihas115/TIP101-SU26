def reverse_string(my_str):
    pass

my_str = "live"
print(reverse_string(my_str))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", "", "| got:", reverse_string(""))

print("Test 2 - single character string")
print("  expected:", "x", "| got:", reverse_string("x"))

print("Test 3 - all-same-character string")
print("  expected:", "mmmm", "| got:", reverse_string("mmmm"))

print("Test 4 - mixed case string")
print("  expected:", "EdoC", "| got:", reverse_string("CodE"))

print("Test 5 - string with punctuation and whitespace")
print("  expected:", "!dlrow ,olleH", "| got:", reverse_string("Hello, world!"))

print("Test 6 - palindrome string reverses to itself")
print("  expected:", "racecar", "| got:", reverse_string("racecar"))
