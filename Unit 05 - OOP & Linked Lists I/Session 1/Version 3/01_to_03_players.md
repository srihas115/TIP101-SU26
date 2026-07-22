# Problem 1: Player Class

Step 1: Copy the following code into your IDE.


Step 2: Instantiate an instance of the class `Player` and store it in a variable named `player_one`.


- The `Player` object should have the `character` `"Yoshi"` and the `kart` `"Super Blooper"`.


```python
class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
        self.items = []
```


<details>
  <summary>✨ <b>AI Hint: Intro to Object Oriented Programming</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem may require you to be familiar with Object Oriented Programming (OOP) basics, including classes, instances, objects, and constructors. To help, we've included an "intro to OOP" review [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)


You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Can you help me understand OOP conceptually, using analogies to real-world objects?"*


Once you understand the concept, you can also ask follow-up questions like:


*"Can you provide an example of a class, instance, and constructor in python?"*


*"What does `self` mean in Python, and how is it used in OOP?"*
</details>

---

<!-- Merged from Problem 2: Get Player.md -->

# Problem 2: Get Player

Step 1: Using the `Player` class from Problem 1, add the following `get_player()` method to your code:


```python
def get_player(self):
    return f"{self.character} driving the {self.kart}"
```

Step 2: Create a second instance of `Player` in a variable named `player_two`.


- The `Player` object created should have `character` `"Bowser"` and `kart` `"Pirahna Prowler"`.


Step 3: Use the method `get_player()` below to print out `"Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler"`.


<details>
  <summary>✨ <b>AI Hint: Class Methods</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This question requires you to be familiar with class methods, which are functions attached to an object. To help, we've included more info [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)


If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Please provide 2-3 examples of how Class Methods are used in Python, and explain how each one works."*


You might also want to ask questions like:


*"Can you explain the difference between class methods, instance methods, and functions?"*
</details>

---

<!-- Merged from Problem 3: Update Kart.md -->

# Problem 3: Update Kart

Players might want to update their choice of kart for their next race.


Update `player_one` so that their kart is `"Dolphin Dasher"` instead of it's current value, `"Super Blooper"`.


Example Usage:


```python
print(player_one.get_player())

# < your code to update kart>

print(player_one.get_player())
```

Example Output:


```
Yoshi driving the Super Blooper
Yoshi driving the Dolphin Dasher
```


<details>
  <summary>✨ <b>AI Hint: Class Attributes</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem may require you to be familiar with class attributes, which are variables attached to an object. To help, we've included more info [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)


If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Please provide 2-3 examples of how Class Attributes are used in Python, and explain how each one works."*
</details>
