class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]
