# Problem 3: Valid Palindrome

Write a function `valid_palindrome()` that takes in a string `s` as a parameter and returns `True` if `s` can be a palindrome after deleting at most one character from it and `False` otherwise.


```python
def valid_palindrome(s):
    pass
```

Example Usage:


```python
s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
```

Example Output:


```python
True
True
False
```


### 💡 Hint: Helper Functions


This problem may benefit from a helper function!


If you find your functions getting too long or performing lots of different tasks, it might be a good indicator that you should add a helper function. Helper functions are functions we write to implement a subtask of our primary task.


We can then call our function inside of our main function, to keep our main function shorter and easy to read.


Example: Calculating a Bill Total


```python
# Helper Function: Calculate the price of one item
def calculate_price(item_price, quantity):
    return item_price * quantity

# Primary Function: Calculate total cost of bill
def calculate_total(bill):
    total = o
    for item_price, quantity in bill.items():
        # Call helper function
        total += calculate_price(item_price, quantity)
    return total
```

Creating helper functions helps us follow the Single Responsibility Principle (SRP) which says that a function should perform only a single task or action. SRP helps us create clean, readable, and maintainable code!
