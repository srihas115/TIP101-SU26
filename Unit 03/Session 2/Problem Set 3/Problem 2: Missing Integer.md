# Problem 2: Missing Integer

Write a function `find_missing_positive()` that takes in a *sorted* list of integers `nums` that always starts at `1`, and returns the smallest missing positive integer.


```python
def find_missing_positive(nums):
    pass
```

Example Usage:


```python
nums1 = [1,2,3,5,6,10]
print(find_missing_positive(nums1))

nums2 = [1,2,3,4,5]
print(find_missing_positive(nums2))
```

Example Output:


```python
4
6
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
