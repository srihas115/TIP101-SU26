# Problem 5: Restock Inventory

Write a function `restock_inventory()` that updates an inventory dictionary based on a restock list. It accepts two parameters:


- `current_inventory`: a dictionary where each key-value pair represents an item and its current stock in the inventory

- `restock_list`: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory


If an item in `restock_list` is not present in the `current_inventory`, it should be added. The function should return the updated dictionary `current_inventory`.


```python
def restock_inventory(current_inventory, restock_list):
    pass
```

Example Input:


```python
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
```

Example Output:


```python
{
    "apples": 4 0,
    "bananas": 15,
    "oranges": 30,
    "pears": 5
}
```


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
