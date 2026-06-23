# Problem 2: Dictionary Difference

Write a function `dict_difference()` that takes two dictionaries and returns a new dictionary that contains only the key-value pairs found only in the first dictionary but not in the second.


```python
def dict_difference(d1, d2):
    pass
```

Example Input:


```python
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))
```

Example Output: `{'a': 1, 'c': 3, 'd': 4}`


### 💡 Hint: Accessing Keys, Values, and Key-Value Pairs


This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To explore how to access the keys, values, and key-value pairs reference the Unit cheatsheet. For specific examples of looping over a dictionary, ask a generative AI tool to provide an example or search for existing examples using a search engine.


### 💡 Hint: Looping over Key-Value Pairs


This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To loop over both keys and values simultaneously, we often use the following syntax:


```python
for k, v in dict.items():
    # function body here
```

For a deeper understanding of how this syntax works, ask a generative AI tool to break down looping over a dictionary with `dict.items()` or search for existing examples using a search engine.
