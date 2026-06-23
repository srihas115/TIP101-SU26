# Problem 4: Catch Pokemon

Update the `Pokemon` class with a new method `catch()` that takes in no parameters except `self`.


The method should update the Pokemon's `is_caught` attribute to `True` and not return any value.


```python
class Pokemon():
	...
	
	def catch(self):
		pass
```

Example Usage:


```python
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()
```

Example Output:


```python
{'name': 'rattata', 'types': ['Normal'], 'is_caught': False} # First print statement
{'name': 'rattata', 'types': ['Normal'], 'is_caught': True}  # Second print statement
```


### ✨ AI Hint: Writing Methods


*Key Skill: Use AI to explain code concepts*


This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:


- Check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)

- Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python
