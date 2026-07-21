def reverse_vowels(s):
    pass

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", "", "| got:", reverse_vowels(""))

print("Test 2 - no vowels (unchanged)")
print("  expected:", "xyz", "| got:", reverse_vowels("xyz"))

print("Test 3 - all vowels")
print("  expected:", "uoiea", "| got:", reverse_vowels("aeiou"))

print("Test 4 - mixed case vowels")
print("  expected:", "UOIEA", "| got:", reverse_vowels("AEIOU"))

print("Test 5 - single vowel (unchanged)")
print("  expected:", "a", "| got:", reverse_vowels("a"))
