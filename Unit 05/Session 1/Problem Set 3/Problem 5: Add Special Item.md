# Problem 5: Add Special Item

Players can pick up special items as they race.


Update the `Player` class with a new method `add_item()` that takes in one parameter, `item_name`.


The method should validate the `item_name`.


- If the item is valid, add `item_name` to the player’s `items` attribute.

- The method does not need to return any values.


`item_name` is valid if it has one of the following values: `"banana"`, `"green shell"`, `"red shell"`, `"bob-omb"`, `"super star"`, `"lightning"`, `"bullet bill"`.


```python
class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []
		
	def add_item(self, item_name):
		pass
```

Example Usage:


```python
player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

player_one.add_item("red shell")
# items = ["red shell"]

player_one.add_item("super star")
# items = ["red shell", "super star"]

player_one.add_item("super smash")
# items = ["red shell", "super star"]
```


<details>
  <summary>✨ <b>AI Hint: Writing Methods</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:


- Check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)

- Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python
</details>
