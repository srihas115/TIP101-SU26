# Problem 3: Print Pair

Write a function `print_pair()` that takes in a dictionary `dictionary` and a key `target` as parameters. The function looks for the `target` and when found, it prints the key and it's associated value as `"Key: <key>"` followed by `"Value: <value>"`. If `target` is not in `dictionary`, print `"That pair does not exist!"`.


```python
def print_pair(dictionary, target):
    pass
```

Example Usage:


```python
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
```

Example Output:


```
Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants
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
