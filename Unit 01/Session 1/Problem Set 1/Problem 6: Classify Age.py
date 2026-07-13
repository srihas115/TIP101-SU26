def classify_age(age):
    pass

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - age exactly 18 (boundary, adult)")
print("  expected:", "adult", "| got:", classify_age(18))

print("Test 2 - age 17 (just under boundary, child)")
print("  expected:", "child", "| got:", classify_age(17))

print("Test 3 - age 0")
print("  expected:", "child", "| got:", classify_age(0))

print("Test 4 - negative age")
print("  expected:", "child", "| got:", classify_age(-5))

print("Test 5 - large age")
print("  expected:", "adult", "| got:", classify_age(150))
