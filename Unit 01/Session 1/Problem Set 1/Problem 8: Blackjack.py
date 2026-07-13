def blackjack(score):
    pass

blackjack(21)
blackjack(24)
blackjack(19)
blackjack(10)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - score 17 (boundary, Nice hand!)")
print("  expected printed output: Nice hand!")
blackjack(17)

print("Test 2 - score 16 (just under boundary, Hit me!)")
print("  expected printed output: Hit me!")
blackjack(16)

print("Test 3 - score 0")
print("  expected printed output: Hit me!")
blackjack(0)

print("Test 4 - negative score")
print("  expected printed output: Hit me!")
blackjack(-5)

print("Test 5 - score way over 21")
print("  expected printed output: Bust!")
blackjack(100)
