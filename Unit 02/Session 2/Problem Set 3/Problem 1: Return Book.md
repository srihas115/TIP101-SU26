# Problem 1: Return Book

Write a function `return_book()` that accepts a string `title` and a dictionary `library` as parameters. `library` maps book titles to the number of copies the library currently has in stock. The function should increment the quantity of the book `title` in `library` by 1. If `title` is not in the library, then add it and set quantity to 1. Return the updated `library` dictionary.


```python
def return_book(title, library):
    pass
```

Example Usage:


```python
library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)
```

Example Output:


```python
{'The Hobbit': 2, '1984': 2, 'The Great Gatsby': 4}
{'The Hobbit': 2, '1984': 1, 'The Great Gatsby': 4, 'The Giver': 1}
```


### ✨ AI Hint: Accessing Values in a Dictionary


*Key Skill: Use AI to explain code concepts*


This question will require you to use keys to access their corresponding values in a dictionary. There are two common ways to access values in a dictionary. Try asking ChatGPT or GitHub copilot:


*"You're an expert computer science tutor. Please show me the two most common ways to access values in a dictionary in Python, and explain how each one works."*


Then open the next hint to see the answer!


### 💡 Hint: Dictionary Access options


The two common ways to access values in a dictionary are square bracket notation `d[key]` and the `get()` method.


The Unit 2 cheatsheet includes a more thorough breakdown of these two options. If you still feel confused after reviewing the cheatsheet, try asking generative AI to help you understand!
