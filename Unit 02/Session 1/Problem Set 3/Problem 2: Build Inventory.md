# Problem 2: Build Inventory

Write a function `build_inventory()` that takes in a list of `product_names` and a corresponding list of `product_prices` as parameters. The function returns a dictionary representing the inventory of a small store. Each product name in `product_names` should be a key in the dictionary and the corresponding value should be the item price.


`product_names[i]` should be paired with `product_prices[i]` in the dictionary where `0` <= `i` <= `len(product_names)`. You may assume that `product_names` and `product_prices` are the same length.


```python
def build_inventory(product_names, product_prices):
    pass
```

Example Input:


```python
product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))
```

Example Output:


```python
{'Apple': 0.99, 'Banana': 0.5, 'Orange': 0.75}
```


### ✨ AI Hint: Dictionaries


*Key Skill: Use AI to explain code concepts*


This question requires you to create a dictionary.


If you are unfamiliar with what a dictionary is, or how to create a dictionary, you can learn about Python dictionaries using a generative AI tool, like this:


*"You're an expert computer science tutor. Please explain what a dictionary is in Python, and provide a simple code example of how to create one."*


After you get your answer, you can also ask follow up questions:


*"How is a dictionary different from a list? Can you show me examples of both?"*
