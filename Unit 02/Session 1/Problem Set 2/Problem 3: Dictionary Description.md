# Problem 3: Dictionary Description

The following function `get_description()` takes in a dictionary `info` and a list `keys` as parameters. For each key in `keys`, the function prints the value associated with that key in `info` and prints `None` if the key does not exist in `info`.


However, the function has a bug! Copy the function into your IDE and run the code. Work with your group members to find the cause of the bug and correctly implement the function.


```python
def get_description(info, keys):
    for key in keys:
	    print(info[key])
```

Example Input:


```python
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
```

*Expected* Output:


```python
Tom
engineer
None
```

*Note*: The actual input you see when you run the provided code without fixing the bug may be different!


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
