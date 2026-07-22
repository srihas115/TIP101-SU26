# Problem 4: Valid Card

Update the `Card` class with a new method `is_valid()` that takes in no parameters except `self`. The method should return `True` if:


- The `suit` is one of the following values: `"Hearts"`, `"Spades"`, `"Clubs"`, `"Diamonds"`

- The `rank` is one of the following values: `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"`, `"8"`, `"9"`, `"10"`, `"Jack"`, `"Queen"`, `"King"`, `"Ace"`


Otherwise, the method should return `False`


```python
class Card():
	...
	
	def is_valid(self):
		pass
```

Example Usage:


```python
my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())
```

Example Output:


```
True
False
```


<details>
  <summary>✨ <b>AI Hint: Writing Methods</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to write your own method! Try it yourself, but if you get stuck, you can:


- Check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)

- Use an AI tool like ChatGPT or GitHub Copilot to show you examples of how to write methods in Python
</details>
