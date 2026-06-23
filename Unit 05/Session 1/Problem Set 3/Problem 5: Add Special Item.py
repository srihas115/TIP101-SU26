class Player():
    def  __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def add_item(self, item_name):
        pass

player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

player_one.add_item("red shell")
# items = ["red shell"]

player_one.add_item("super star")
# items = ["red shell", "super star"]

player_one.add_item("super smash")
# items = ["red shell", "super star"]
