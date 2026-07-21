def max_vowels(s, k):
    pass

s = "abciiidef"
print(max_vowels(s, 3))

print(max_vowels(s, 5))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no vowels at all")
print("  expected:", 0, "| got:", max_vowels("xyz", 2))

print("Test 2 - k equals the length of s (whole string is the window)")
print("  expected:", 3, "| got:", max_vowels("aeixyz", 6))

print("Test 3 - k is 1")
print("  expected:", 1, "| got:", max_vowels("xay", 1))
