# Problem 1: Counting Down

A recursive function is a function that calls itself within the body of the function.


Step 1: Copy this code into your IDE and run it.


Step 2: Then create another function `countdown_iterative()` that produces the same output without using recursion.


Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?


```python
def countdown(n):
	if n > 0:
		print(n)
		countdown(n - 1)
		
countdown(5)
```

Example Usage:


```python
# Example Input: 5
```

Example Output:


```python
# Expected Output:
# 5
# 4
# 3
# 2
# 1
# Explanation: The function prints numbers starting at 5 and counts down by 1 until it reaches 1.
```


### 💡 Hint: Recursion


This problem requires you to understand recursion and the differences between iteration and recursion. For reference, check out the [Unit 7 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/7#!cheatsheet).
