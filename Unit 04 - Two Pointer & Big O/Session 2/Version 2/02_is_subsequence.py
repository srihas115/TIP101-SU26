def is_subsequence(s, t):
    pass

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty s (empty string is a subsequence of anything)")
print("  expected:", True, "| got:", is_subsequence("", "abc"))

print("Test 2 - s equals t")
print("  expected:", True, "| got:", is_subsequence("abc", "abc"))

print("Test 3 - s longer than t")
print("  expected:", False, "| got:", is_subsequence("abcd", "abc"))

print("Test 4 - empty t, non-empty s")
print("  expected:", False, "| got:", is_subsequence("a", ""))
