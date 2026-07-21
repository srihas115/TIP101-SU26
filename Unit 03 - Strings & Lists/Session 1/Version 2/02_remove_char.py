def remove_char(s, n):
    pass

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - remove first valid index (n=1) from a string")
print("  expected:", "bc", "| got:", remove_char("abc", 1))

print("Test 2 - remove second-to-last valid index (n=len(s)-1)")
print("  expected:", "ab", "| got:", remove_char("abc", 2))

print("Test 3 - all-same-character string")
print("  expected:", "zzz", "| got:", remove_char("zzzz", 2))

print("Test 4 - mixed case string, removing an uppercase char")
print("  expected:", "cODE", "| got:", remove_char("cODE".replace('O','O'), 0) if False else remove_char("ScODE", 1))

print("Test 5 - string with punctuation/whitespace character removed")
print("  expected:", "hillo", "| got:", remove_char("hi llo", 2))
