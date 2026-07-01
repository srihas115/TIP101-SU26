# UPI
# Understand 
# Input: pokemon object (starter_pokemon)
# Output: a list of evolved pokemon and starter pokemon
# Plan: empty list and traverse through like linked list
# Implement: (below)

class Pokemon():
    def  __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

def get_evolutionary_line(starter_pokemon):
    output = []
    curr = starter_pokemon
    
    output.append(starter_pokemon.name)
    
    while(curr.evolution is not None):
        output.append(curr.evolution.name)
        curr = curr.evolution
    
    return output   
        
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
