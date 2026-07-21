def is_pangram(my_str):
    pass

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string is not a pangram")
print("  expected:", False, "| got:", is_pangram(""))

print("Test 2 - single character string is not a pangram")
print("  expected:", False, "| got:", is_pangram("a"))

print("Test 3 - all 26 letters lowercase exactly once")
print("  expected:", True, "| got:", is_pangram("abcdefghijklmnopqrstuvwxyz"))

print("Test 4 - all 26 letters with mixed case")
print("  expected:", True, "| got:", is_pangram("ABCdefGHIjklMNOpqrSTUvwxYZ"))

print("Test 5 - pangram with punctuation and repeated letters")
print("  expected:", True, "| got:", is_pangram("Pack my box with five dozen liquor jugs!"))

print("Test 6 - missing one letter (z) should not be a pangram")
print("  expected:", False, "| got:", is_pangram("abcdefghijklmnopqrstuvwxy"))
