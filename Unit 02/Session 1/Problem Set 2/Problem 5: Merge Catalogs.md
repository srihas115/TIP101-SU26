# Problem 5: Merge Catalogs

Write a function `merge_catalogs()` that combines two product catalogs, `catalog1` and `catalog2` as parameters. Each parameter is a dictionary where each key-value pair represents a product name and its price, respectively. If the same product exists in both catalogs, the price from the second catalog should overwrite the price in the first. Return the updated first catalog dictionary.


```python
def merge_catalogs(catalog1, catalog2):
    pass
```

Example Input:


```python
catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
```

Example Output: `{'apple': 1.0, 'banana': 0.75, 'cherry': 1.25}`


### 💡 Hint: Looping over Key-Value Pairs


This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To loop over both keys and values simultaneously, we often use the following syntax:


```python
for k, v in dict.items():
    # function body here
```

For a deeper understanding of how this syntax works, ask a generative AI tool to break down looping over a dictionary with `dict.items()` or search for existing examples using a search engine.
