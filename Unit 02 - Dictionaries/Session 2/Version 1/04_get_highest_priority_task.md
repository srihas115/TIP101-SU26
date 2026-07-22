# Problem 4: Highest Priority Task

Given a dictionary `tasks` where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function `get_highest_priority_task()` that removes the task with the highest priority from the dictionary and returns its name.

If two tasks have the same priority, return the task that comes first in the alphabet.


```python
def get_highest_priority_task(tasks):
	pass
```

Example Usage:


```python
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
```

Example Output:


```
task2
task4
task3
{'task1': 8,'task5': 7}
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
