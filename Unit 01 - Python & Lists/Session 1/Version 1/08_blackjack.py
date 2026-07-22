'''
==============================================================================
    Unit 1: Python & Lists  ·  Session 1  ·  Version 1
    Problem 8: Blackjack

    In the game Blackjack, players try to draw a hand of cards that totals as
    close to 21 as possible. Players "bust" if their cards total more than 21.
    Players say "Hit me!" if they want the dealer to give them another card.

    Write a function called `blackjack()` that takes an integer `score` as a
    parameter. If `score` equals 21, print `"Blackjack!"`. If `score` is
    greater than 21, print `"Bust!"`. If `score` is greater than or equal to
    17 and less than 21, print `"Nice hand!"`. If `score` is less than 17,
    print `"Hit me!"`.

    Example Usage:

    Write your solution for `blackjack` in the space below,
    then click  ▶ Run  to grade it.
    (The full problem, with examples, is in the problem set.)

    ⚠️  Keep the function name `blackjack` and its parameters exactly as given —
        the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    elif score < 17:
        print("Hit me!")

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


'''
==============================================================================
    PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade, test

grade(blackjack)   # ▶ Run this file to validate your solution

'''
==============================================================================
    YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test(21, expected='Blackjack!')   # checks the printed output against this example
