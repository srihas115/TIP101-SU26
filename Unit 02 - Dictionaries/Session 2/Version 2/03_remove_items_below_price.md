# Problem 3: Filter by Price

Write a function that takes in a dictionary of `items` and a `price_threshold` as parameters. The function should iterate through the dictionary and remove all items that has a value less than `price_threshold`. The function also returns a list of all items that are removed. If no item satisfies the condition, return `None`.


```python
def remove_items_below_price(items, price_threshold):
    pass
```

Example Usage:


```python
items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)
```

Example Output:


```python
["banana", "date"]
None
```


<details>
  <summary>💡 <b>Hint: Removing Key-Value Pairs from a Dict</b></summary>

  <br>

This question requires you to remove key-value pairs from a dictionary. Just like with a list, you can use the `pop()` method to remove a key-value pair from a dictionary. For example, if you have a dictionary `my_dict` and you want to remove the key-value pair with key `my_key`, you can use the following code:


```python
my_dict.pop('my_key')
```

Be careful: If you try to remove a key-value pair **while** looping through the dictionary, you may encounter a `RuntimeError`. To avoid this, you can create a list of keys to remove and then loop through that list to remove the key-value pairs from the dictionary.
</details>
