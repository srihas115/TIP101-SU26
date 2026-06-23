# Problem 1: Battle Pokemon

Given the `Pokemon` class below, copy the code and add it to your IDE.


```python
class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		pass
```

Then, write a method `attack()` that takes in a `Pokemon` object `opponent` and decreases `opponent`'s `hp` by their self's `damage` amount.


If damaging the opponent leads to the opponent having an `hp` of 0 or less, the function should set the opponent's `hp` to 0 and print out `"<Opponent name> fainted>`.


Otherwise, the function should print out `"<Pokemon name> dealt <damage> damage to <opponent name>"`.


Example Usage:


```python
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30)

opponent = bulbasaur
pikachu.attack(opponent)
```

Example Output: `Pikachu dealt 20 damage to Bulbasaur`


### ✨ AI Hint: Writing Methods


*Key Skill: Use AI to explain code concepts*


This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:


- Check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)

- Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python
