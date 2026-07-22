'''
==============================================================================
  Unit 5: OOP & Linked Lists I  ·  Session 2  ·  Version 1
  Problem 1: Battle Pokemon
  Write your solution in the space provided below, then click ▶ Run to validate it.
  (Full instructions and examples are in the problem set.)

  ⚠️  Keep every class, method, and function name exactly as the problem gives it,
      and use the exact variable names it asks for — the problem set solution validator looks those up
      by name (they're case-sensitive). If it can't find one, the results will tell
      you which name is missing.
==============================================================================
'''


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


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade

grade(Pokemon)   # ▶ Run this file to validate your work
