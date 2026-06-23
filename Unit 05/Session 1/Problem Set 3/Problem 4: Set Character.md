# Problem 4: Set Character

In the previous exercise, we accessed and modified a player’s `kart` attribute directly. Instead of allowing users to update their player directly, it is common to create **setter methods** that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.


Update your `Player` class with a method `set_character()` that takes in one parameter `name`.


- If `name` is valid, it should update the player’s `character` attribute to have value `name` and print `"Character updated"`.

- Otherwise, it should print out `"Invalid character"`.


Valid character names are `"Mario"`, `"Luigi"`, `"Peach"`, `"Yoshi"`, `"Toad"`, `"Wario"`, `"Donkey Kong"`, and `"Bowser"`.


```python
class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []
		
	def set_player(self, name):
		pass
```

Example Usage:


```python
player_one.set_player("Peach")
player_two.set_player("Kermit")
```

Example Output:


```python
Character updated
Invalid character
```


<details>
  <summary>✨ <b>AI Hint: Writing Methods</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:


- Check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)

- Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python
</details>
