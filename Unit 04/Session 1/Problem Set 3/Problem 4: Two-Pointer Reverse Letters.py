def reverse_only_letters(s):
    pass

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - no letters (all punctuation, unchanged)")
print("  expected:", "---", "| got:", reverse_only_letters("---"))

print("Test 2 - all letters (simple full reverse)")
print("  expected:", "cba", "| got:", reverse_only_letters("abc"))

print("Test 3 - single letter")
print("  expected:", "a", "| got:", reverse_only_letters("a"))

print("Test 4 - empty string")
print("  expected:", "", "| got:", reverse_only_letters(""))
