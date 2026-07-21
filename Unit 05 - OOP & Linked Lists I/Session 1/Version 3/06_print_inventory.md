# Problem 6: Print Inventory

Update the `Player` class with a method `print_inventory()` that accepts no parameters except for self.


The method should print the name and quantity of each item in a player’s items list.


- If the player has no items, the function should print `"Inventory empty"`.


```python
class Player():
	...
	
	def print_inventory(self):
		pass
```

Example Usage:


```python
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()
```

Example Output:


```python
Inventory: banana: 2, bob-omb: 1, super star: 1
Inventory empty
```
