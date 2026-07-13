def find_the_needle(haystack, needle):
    pass

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty needle (found at the start)")
print("  expected:", 0, "| got:", find_the_needle("hello", ""))

print("Test 2 - needle equals haystack")
print("  expected:", 0, "| got:", find_the_needle("abc", "abc"))

print("Test 3 - needle not found")
print("  expected:", -1, "| got:", find_the_needle("abc", "xyz"))

print("Test 4 - single-character haystack and needle, matching")
print("  expected:", 0, "| got:", find_the_needle("a", "a"))
