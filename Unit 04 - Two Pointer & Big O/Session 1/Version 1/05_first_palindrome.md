# Problem 5: Palindrome

Write a function `first_palindrome()` that takes in a list of strings `words` as a parameter and returns the first palindromic string in the list. A string is **palindromic** if it reads the same forward and backward. If there is no such string, return an empty string `""`


```python
def first_palindrome(words):
    pass
```

Example Usage:


```python
words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
```

Example Output:


```
ada
racecar
```


<details>
  <summary>💡 <b>Hint: Helper Functions</b></summary>

  <br>

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
</details>

Creating helper functions helps us follow the Single Responsibility Principle (SRP) which says that a function should perform only a single task or action. SRP helps us create clean, readable, and maintainable code!
