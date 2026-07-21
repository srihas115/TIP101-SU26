def is_palindrome(s):
    pass

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string (vacuously a palindrome)")
print("  expected:", True, "| got:", is_palindrome(""))

print("Test 2 - single character")
print("  expected:", True, "| got:", is_palindrome("a"))

print("Test 3 - two identical characters")
print("  expected:", True, "| got:", is_palindrome("aa"))

print("Test 4 - two different characters")
print("  expected:", False, "| got:", is_palindrome("ab"))

print("Test 5 - all-same-character string")
print("  expected:", True, "| got:", is_palindrome("aaaa"))
