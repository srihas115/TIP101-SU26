# Problem 1: Highest Exponent

Write a function `find_highest_exponent()` that takes in an integer `base` and an integer `limit` as parameters. The function returns the highest exponent for which a given `base` raised to that exponent is less than or equal to `limit`.


```python
def find_highest_exponent(base, limit):
    pass
```

Example Usage:


```python
exp = find_highest_exponent(2, 100)
print(exp)

exp2 = find_highest_exponent(3, 5)
print(exp2)
```

Example Output:


```python
# 2^6 = 64 and 2^7 = 128
6
# 3^1 = 3 and 3^2 = 9
1
```


<details>
  <summary>✨ <b>AI Hint: While Loops</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This exercise may require you to use a while loop. If you aren't sure what a while loop is, or how it differs from a for loop, try asking ChatGPT or GitHub copilot:


*"You're an expert computer science tutor. What is the difference between a for loop and a while loop in Python? Please provide examples of each."*


Then open the next hint to see our answer!
</details>
<details>
  <summary>💡 <b>Hint: While Loops (more detail)</b></summary>

  <br>

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
</details>
