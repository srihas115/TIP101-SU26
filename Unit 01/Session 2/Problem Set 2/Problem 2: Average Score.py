def average(scores):
    pass

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-element list")
print("  expected:", 50.0, "| got:", average([50]))

print("Test 2 - all elements equal")
print("  expected:", 7.0, "| got:", average([7,7,7]))

print("Test 3 - list containing zero")
print("  expected:", 3.0, "| got:", average([0,3,6]))

print("Test 4 - negative numbers")
print("  expected:", -2.0, "| got:", average([-1,-2,-3]))
