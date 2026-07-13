class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        pass

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-digit numeric rank")
print("  expected:", 2, "| got:", Card("Hearts", "2").get_value())

print("Test 2 - rank '10'")
print("  expected:", 10, "| got:", Card("Clubs", "10").get_value())

print("Test 3 - rank 'Queen'")
print("  expected:", 12, "| got:", Card("Diamonds", "Queen").get_value())

print("Test 4 - rank 'King'")
print("  expected:", 13, "| got:", Card("Clubs", "King").get_value())

print("Test 5 - invalid rank")
print("  expected:", None, "| got:", Card("Hearts", "Joker").get_value())
