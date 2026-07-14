def hello_world():
    print("Hello world!")


# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - basic call")
print("  expected printed output: Hello world!")
hello_world()

print("Test 2 - calling twice in a row still prints each time")
print("  expected printed output (two lines): Hello world! / Hello world!")
hello_world()
hello_world()
