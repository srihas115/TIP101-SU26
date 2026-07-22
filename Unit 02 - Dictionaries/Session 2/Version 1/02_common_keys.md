# Problem 2: Keys in Common

Write a function that takes in two dictionaries, `dict1` and `dict2` and finds all keys common to both dictionaries. The function returns a list of common keys.


```python
def common_keys(dict1, dict2):
	pass
```

Example Usage:


```python
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
```

Example Output:


```
['b', 'c']
```


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
