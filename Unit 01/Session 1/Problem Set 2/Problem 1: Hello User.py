def greet_user(name):
    print("Hello", name)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - basic name")
print("  expected printed output: Hello Michael")
greet_user("Michael")

print("Test 2 - empty string name")
print("  expected printed output: Hello ")
greet_user("")

print("Test 3 - single character name")
print("  expected printed output: Hello X")
greet_user("X")

print("Test 4 - name with spaces")
print("  expected printed output: Hello Mary Jane")
greet_user("Mary Jane")
