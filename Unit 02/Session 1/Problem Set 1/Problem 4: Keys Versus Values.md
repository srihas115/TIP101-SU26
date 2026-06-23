# Problem 4: Keys Versus Values

Write a function `keys_v_values()` that takes in a dictionary `dictionary` whose keys and values are both integers. *Using at least one loop*, the function should find the sum of all keys in the dictionary and the sum of all values.

If the sum of all keys is greater than the sum of all values, the function should return the string `"keys"`.

If the sum of all values is greater than the sum of all keys, the function should return the string `"values"`.

If keys and values have equal sums, the function should return the string `"balanced"`.


```python
def keys_v_values(dictionary):
    pass
```

Example Usage:


```python
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
```

Example Output:


```python
values
keys
```


<details>
  <summary>💡 <b>Hint: Accessing Keys, Values, and Key-Value Pairs</b></summary>

  <br>

This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To explore how to access the keys, values, and key-value pairs reference the Unit cheatsheet. For specific examples of looping over a dictionary, ask a generative AI tool to provide an example or search for existing examples using a search engine.
</details>
