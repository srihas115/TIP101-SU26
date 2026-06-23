# Problem 1: Cast Vote

Write a function `cast_vote()` that records a vote for a candidate in an election. The function accepts a dictionary `votes` that maps candidates to their current number of votes and a string `candidate` that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.


```python
def cast_vote(votes, candidate):
    pass
```

Example Usage:


```python
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
```

Example Output:


```python
{'Alice': 6, 'Bob': 3}
{'Alice': 6, 'Bob': 3, 'Gina': 1}
```


### ✨ AI Hint: Accessing Values in a Dictionary


*Key Skill: Use AI to explain code concepts*


This question will require you to use keys to access their corresponding values in a dictionary. There are two common ways to access values in a dictionary. Try asking ChatGPT or GitHub copilot:


*"You're an expert computer science tutor. Please show me the two most common ways to access values in a dictionary in Python, and explain how each one works."*


Then open the next hint to see the answer!


### 💡 Hint: Dictionary Access options


The two common ways to access values in a dictionary are square bracket notation `d[key]` and the `get()` method.


The Unit 2 cheatsheet includes a more thorough breakdown of these two options. If you still feel confused after reviewing the cheatsheet, try asking generative AI to help you understand!
