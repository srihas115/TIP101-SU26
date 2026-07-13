def partition_label(s):
    pass

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", [], "| got:", partition_label(""))

print("Test 2 - single character")
print("  expected:", [1], "| got:", partition_label("a"))

print("Test 3 - all-same-character string (one partition)")
print("  expected:", [4], "| got:", partition_label("aaaa"))

print("Test 4 - all unique characters (each its own partition)")
print("  expected:", [1,1,1,1], "| got:", partition_label("abcd"))
