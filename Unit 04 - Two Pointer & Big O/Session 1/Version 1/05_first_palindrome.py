def first_palindrome(words):
    pass

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", "", "| got:", first_palindrome([]))

print("Test 2 - single-element list, is a palindrome")
print("  expected:", "level", "| got:", first_palindrome(["level"]))

print("Test 3 - single-element list, not a palindrome")
print("  expected:", "", "| got:", first_palindrome(["hello"]))

print("Test 4 - single-character words (trivially palindromic)")
print("  expected:", "a", "| got:", first_palindrome(["a", "b"]))
