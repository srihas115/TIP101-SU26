def reverse_prefix(word, ch):
    pass

word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - ch is the first character (single-char prefix, no visible change)")
print("  expected:", "abc", "| got:", reverse_prefix("abc", "a"))

print("Test 2 - ch is the last character (full reversal)")
print("  expected:", "cba", "| got:", reverse_prefix("abc", "c"))

print("Test 3 - empty word")
print("  expected:", "", "| got:", reverse_prefix("", "a"))

print("Test 4 - ch appears multiple times, uses the first occurrence")
print("  expected:", "cbaabc", "| got:", reverse_prefix("abcabc", "c"))
