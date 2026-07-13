class Player():
    def  __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def set_player(self, name):
        pass

player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Mario", "Standard Kart M")
player_one.set_player("Peach")
player_two.set_player("Kermit")

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - valid character name")
p1 = Player("Yoshi", "Super Blooper")
print("  expected printed output: Character updated")
p1.set_player("Mario")
print("  expected character after:", "Mario", "| got:", p1.character)

print("Test 2 - invalid character name (unchanged)")
p2 = Player("Yoshi", "Super Blooper")
print("  expected printed output: Invalid character")
p2.set_player("Kermit")
print("  expected character after:", "Yoshi", "| got:", p2.character)

print("Test 3 - valid character name (Bowser)")
p3 = Player("Toad", "Rocket Star")
print("  expected printed output: Character updated")
p3.set_player("Bowser")
print("  expected character after:", "Bowser", "| got:", p3.character)
