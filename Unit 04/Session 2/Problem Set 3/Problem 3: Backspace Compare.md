# Problem 3: Backspace Compare

Write a function `backspace_compare()` that takes in two strings `s` and `t` as parameters that both might have the backspace character `#`. The backspace character removes the character in front of it. The function returns `True` if they are equal when both are typed into empty text editors and `False` otherwise. Note that after backspacing an empty text, the text will continue empty.


```python
def backspace_compare(s, t):
    pass
```

Example Usage:


```python
s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))
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
