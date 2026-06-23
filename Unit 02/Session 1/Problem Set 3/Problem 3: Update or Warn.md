# Problem 3: Update or Warn

Write a function `update_or_warn()` that takes in a dictionary `records`, a key `item`, and a new value `update_value` as parameters. The function updates the value of `item` in `records` with `update_value` if `item` exists. If `item` does not exist, it should print `"<item> not found!"` and not modify the dictionary.


```python
def update_or_warn(records, item, update_value):
    pass
```

Example Usage:


```python
records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
# Print the input dictionary after running the function to check if it was modified
print(records)
update_or_warn(records, "banana", 5)
print(records)
```

Example Output:


```python
grape not found!
{'apple': 1, 'banana': 2, 'orange': 3}
{'apple': 1, 'banana': 5, 'orange': 3}
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
