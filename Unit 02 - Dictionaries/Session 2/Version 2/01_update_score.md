# Problem 1: Update Score

Write a function `update_score()` that takes in a dictionary `scores` that maps player names to current scores, a string `player`, and an integer `points` as parameters. The function adds the `points` to the current score of `player` in the dictionary and returns the updated dictionary. If the player does not exist in `scores`, then add them.


```python
def update_score(scores, players, points):
    pass
```

Example Usage:


```python
scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)
```

Example Output:


```
{'Alice': 110, 'Bob': 90}
{'Alice': 110, 'Bob': 90, 'Calvin': 20}
{'Alice': 110, 'Bob': 90, 'Calvin': 25}
```


<details>
  <summary>✨ <b>AI Hint: Accessing Values in a Dictionary</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This question will require you to use keys to access their corresponding values in a dictionary. There are two common ways to access values in a dictionary. Try asking ChatGPT or GitHub copilot:


*"You're an expert computer science tutor. Please show me the two most common ways to access values in a dictionary in Python, and explain how each one works."*


Then open the next hint to see the answer!
</details>
<details>
  <summary>💡 <b>Hint: Dictionary Access options</b></summary>

  <br>

The two common ways to access values in a dictionary are square bracket notation `d[key]` and the `get()` method.


The Unit 2 cheatsheet includes a more thorough breakdown of these two options. If you still feel confused after reviewing the cheatsheet, try asking generative AI to help you understand!
</details>
