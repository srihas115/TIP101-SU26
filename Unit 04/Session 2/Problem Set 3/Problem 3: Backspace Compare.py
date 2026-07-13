def backspace_compare(s, t):
    pass

s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - both empty strings")
print("  expected:", True, "| got:", backspace_compare("", ""))

print("Test 2 - both fully backspaced to empty")
print("  expected:", True, "| got:", backspace_compare("a#", "b#"))

print("Test 3 - backspace on empty text does nothing")
print("  expected:", True, "| got:", backspace_compare("#abc", "abc"))

print("Test 4 - trailing backspaces beyond all content")
print("  expected:", True, "| got:", backspace_compare("abc###", ""))
