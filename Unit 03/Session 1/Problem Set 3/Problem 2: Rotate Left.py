def rotate_left(s, n):
    pass

s = "rotation"
print(rotate_left(s, 2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - n is 1")
print("  expected:", "otationr", "| got:", rotate_left("rotation", 1))

print("Test 2 - n equals the string length (full rotation, unchanged)")
print("  expected:", "rotation", "| got:", rotate_left("rotation", 8))

print("Test 3 - single-character string, n is 1")
print("  expected:", "a", "| got:", rotate_left("a", 1))

print("Test 4 - all-same-character string")
print("  expected:", "aaaa", "| got:", rotate_left("aaaa", 2))
