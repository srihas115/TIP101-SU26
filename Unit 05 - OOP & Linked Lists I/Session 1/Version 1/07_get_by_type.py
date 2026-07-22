'''
==============================================================================
    Unit 5: OOP & Linked Lists I  ·  Session 1  ·  Version 1
    Problem 7: Get Pokemon
    Write your solution in the space provided below, then click ▶ Run to validate it.
    (Full instructions and examples are in the problem set.)

    ⚠️  Keep every class, method, and function name exactly as the problem gives it,
        and use the exact variable names it asks for — the problem set solution validator looks those up
        by name (they're case-sensitive). If it can't find one, the results will tell
        you which name is missing.
==============================================================================
Understand (input, output, core logic):
Input: list of pokemon instances, and a list
Output: a list of pokemon with same type

Match:

Plan:
Traverse through list and for each element check
if pokemon type match current element
'''


class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
        
    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
    same_type = []
    
    for pokemon in my_pokemon:
        # print(pokemon.name)
        if pokemon_type in pokemon.types:
            # print(pokemon)
            same_type.append(pokemon.name)
            
    return same_type

# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)


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

grade(get_by_type)   # ▶ Run this file to validate your work
