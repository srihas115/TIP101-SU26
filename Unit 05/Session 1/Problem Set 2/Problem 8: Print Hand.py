class Card():
    def  __init__(self, suit, rank, next = None):
        self.suit = suit
        self.rank = rank
        self.next = next

def print_hand(starting_card):
    pass

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print_hand(card_one)
