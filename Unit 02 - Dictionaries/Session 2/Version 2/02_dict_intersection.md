# Problem 2: Dictionary Intersection

Write a function `dict_intersection()` that takes in two dictionaries as parameters and returns a new dictionary containing the key-value pairs found in both dictionaries.


```python
def dict_intersection(d1, d2):
    pass
```

Example Input:


```python
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
```

Example Output: `{'b': 2}`


<details>
  <summary>💡 <b>Hint: Accessing Keys, Values, and Key-Value Pairs</b></summary>

  <br>

This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To explore how to access the keys, values, and key-value pairs reference the Unit cheatsheet. For specific examples of looping over a dictionary, ask a generative AI tool to provide an example or search for existing examples using a search engine.
</details>
<details>
  <summary>💡 <b>Hint: Looping over Key-Value Pairs</b></summary>

  <br>

This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To loop over both keys and values simultaneously, we often use the following syntax:


```python
for k, v in dict.items():
    # function body here
```

For a deeper understanding of how this syntax works, ask a generative AI tool to break down looping over a dictionary with `dict.items()` or search for existing examples using a search engine.
</details>
