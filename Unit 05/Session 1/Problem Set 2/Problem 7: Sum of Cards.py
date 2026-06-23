class Card():
    def  __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #... methods from previous problems

class Hand:
    def __init__(self):
        self.cards = []

    # ... methods from previous problems


def sum_hand(hand):
    pass

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)
