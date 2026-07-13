class Card():
    def  __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

def is_two_pair(player_hand):
    pass

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - only one pair (not two-pair)")
one_pair_hand = [Card("Hearts", "Ace"), Card("Diamonds", "Ace"), Card("Clubs", "4"), Card("Spades", "6"), Card("Hearts", "7")]
print("  expected:", False, "| got:", is_two_pair(one_pair_hand))

print("Test 2 - no pairs at all")
no_pair_hand = [Card("Hearts", "Ace"), Card("Diamonds", "4"), Card("Clubs", "6"), Card("Spades", "7"), Card("Hearts", "9")]
print("  expected:", False, "| got:", is_two_pair(no_pair_hand))

print("Test 3 - clear two-pair with different ranks")
two_pair_hand = [Card("Hearts", "King"), Card("Diamonds", "King"), Card("Clubs", "Queen"), Card("Spades", "Queen"), Card("Hearts", "2")]
print("  expected:", True, "| got:", is_two_pair(two_pair_hand))
