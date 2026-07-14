def countdown(m,n):
    for num in range(m, n-1, -1):
        print(num)

countdown(5,1)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - m equals n (prints just m)")
print("  expected printed output: 3")
countdown(3, 3)

print("Test 2 - m=1, n=1")
print("  expected printed output: 1")
countdown(1, 1)

print("Test 3 - m less than n (nothing to count down, no output)")
print("  expected printed output: (nothing)")
countdown(2, 5)

print("Test 4 - m=3, n=1")
print("  expected printed output: 3 / 2 / 1")
countdown(3, 1)
