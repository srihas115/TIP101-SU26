def longest_uniform_substring(s):
    pass

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", longest_uniform_substring(""))

print("Test 2 - single character")
print("  expected:", 1, "| got:", longest_uniform_substring("a"))

print("Test 3 - all-same-character string")
print("  expected:", 5, "| got:", longest_uniform_substring("aaaaa"))

print("Test 4 - longest run is at the end")
print("  expected:", 5, "| got:", longest_uniform_substring("abccccc"))
