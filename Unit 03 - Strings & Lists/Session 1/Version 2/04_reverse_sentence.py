def reverse_sentence(sentence):
    pass

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", "good no to up am I swear solemnly I", "| got:", reverse_sentence("I solemnly swear I am up to no good"))

print("Test 2 - single word (unchanged)")
print("  expected:", "hello", "| got:", reverse_sentence("hello"))

print("Test 3 - empty string")
print("  expected:", "", "| got:", reverse_sentence(""))

print("Test 4 - two words")
print("  expected:", "world hello", "| got:", reverse_sentence("hello world"))
