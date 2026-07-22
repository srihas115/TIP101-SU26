# Problem 3: Recursive Digits Sum

Given a non-negative integer n, write a function `sum_digits()` that calculates and returns the sum of its digits recursively.


Evaluate the time and space complexity of your solution.


```python
def sum_digits(n):
	pass
```

Example Usage:


```python
# Example Input: 523
```

Example Output:


```
# Expected Output: 10
```


<details>
  <summary>💡 <b>Hint: Finding Digits</b></summary>

  <br>

The [mod operator `%`](https://courses.codepath.org/courses/tip101/unit/2#!cheatsheet) can be used to find the rightmost digit of a number.


```python
126 % 10 #This evaluates to 6
```

[Floor division `//`](https://courses.codepath.org/courses/tip101/unit/2#!cheatsheet) can be used to remove the rightmost digit of a number.


```python
126 // 10 #This evaluates to 12
```
</details>
