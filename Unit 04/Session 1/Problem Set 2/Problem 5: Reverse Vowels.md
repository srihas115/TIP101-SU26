# Problem 5: Reverse Vowels

Write a function `reverse_vowels()` that takes in a string `s` as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider **a**, **e**, **i**, **o**, and **u** as vowels but not **y**. The vowels can appear in both lower and upper cases, more than once.


```python
def reverse_vowels(s):
    pass
```

Example Usage:


```python
s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
```

Example Output:


```python
holle
leotcede
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
