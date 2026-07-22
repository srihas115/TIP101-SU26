# Problem 3: Take from Stock

Write a function `pop_stock()` that takes a dictionary of items `items` that keeps track of an item and its stock quantity, an `item_name`, and a `quantity` to be removed as parameters. The function should remove the specified `quantity` for that item.

If the item does not exist, return the string `"Item does not exist."`

If the specified quantity is greater than the stock, return a string `"Not enough stock."`

If the specified item and quantity do exist within `items`, decrement the item's stock by the specified quantity and return the updated dictionary.


```python
def pop_stock(items, item_name, quantity):
    pass
```

Example Usage:


```python
items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)
```

Example Output:


```
{'chocolate': 20, 'candy': 3, 'chips': 10}
Not enough stock
Item does not exist
{'chocolate': 15, 'candy': 3, 'chips': 10}
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
