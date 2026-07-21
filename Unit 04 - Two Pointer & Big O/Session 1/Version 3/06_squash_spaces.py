def squash_spaces(s):
    pass

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", "", "| got:", squash_spaces(""))

print("Test 2 - only spaces")
print("  expected:", "", "| got:", squash_spaces("     "))

print("Test 3 - single word, no spaces")
print("  expected:", "word", "| got:", squash_spaces("word"))
