# Problem 1: Prime Number

Write a function `is_prime()` that takes in a positive integer `n` and returns `True` if it is a prime number and `False` otherwise. A **prime number** is a number greater than 1 that has no positive divisors other than 1 and itself.


```python
def is_prime(n):
    pass
```

Example Usage:


```python
print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
```

Example Output:


```python
True
False
False
```


### ✨ AI Hint: While Loops


*Key Skill: Use AI to explain code concepts*


This exercise may require you to use a while loop. If you aren't sure what a while loop is, or how it differs from a for loop, try asking ChatGPT or GitHub copilot:


*"You're an expert computer science tutor. What is the difference between a for loop and a while loop in Python? Please provide examples of each."*


Then open the next hint to see our answer!


### 💡 Hint: While Loops (more detail)


For loops and while loops are both used to repeat a block of code, but for loops are iteration based (used to iterate over a sequence) while while loops continues to execute as long as a specified condition is true.


In general, we should use a while loop instead of a for loop when:


- we do not know beforehand the exact number of repetitions we want to do

```python
 # For loop: Repeat for however many elements there are in the list
 for elt in len(lst):
 print(elt)

 # While loop: Repeat until fruit = 'banana'
 # but we're not exactly sure when that will be
 while fruit != 'banana':
 print('Guess my favorite fruit!')
 # Input function returns user's guess
 fruit = input('Enter your guess: ')
```

- we want greater control over our loop variable

```python
 # For loop: Loop variable increases by two each time
 for num in range(1, 10, 2):
 print(num)

 # While loop: Conditionally increase loop variable by different amounts
 num = 1
 while num < 10:
 print(num)
 if num % 2 == 0:
 num += 1
 else:
 num += 2
```

- we want to mutate a variable during the iteration process

```python
 # For loop: Mutating a list inside a for loop can cause unexpected results!
 # Can make loop variable out of sync with list contents
 for elt in lst:
 if elt == 'b':
 lst.remove('b')

 # While loop: The condition and value of the list is checked
 # at the beginning of each iteration, making it safe to modify
 while 'b' in lst:
 lst.remove('b')
```
