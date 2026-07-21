class Pokemon():
    def  __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp # hit points
        self.damage = damage # The amount of damage this pokemon does to its opponent every attack

    def attack(self, opponent):
        if opponent.hp - self.damage <= 0:
            opponent.hp = 0
            print(f"{opponent.name} fainted")
        else:
            opponent.hp -= self.damage
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

        
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30)

opponent = bulbasaur
pikachu.attack(opponent)
