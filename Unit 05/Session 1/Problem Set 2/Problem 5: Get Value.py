class Card():
    ...

    def get_value(self):
        pass

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())
