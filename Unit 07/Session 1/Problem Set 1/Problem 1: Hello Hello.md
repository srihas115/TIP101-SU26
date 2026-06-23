# Problem 1: Hello Hello

A recursive function is a function that calls itself within the body of the function.


Step 1: Copy the recursive function `repeat_hello()` into your IDE and run it.


Step 2: Then create another function `repeat_hello_iterative()` that produces the same output without using recursion.


Compare your iterative (non-recursive) solution to the recursive solution provided. What is similar? What is different?


```python
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
repeat_hello(5)
```


<details>
  <summary>💡 <b>Hint: Recursion</b></summary>

  <br>

This problem requires you to understand recursion and the differences between iteration and recursion. For reference, check out the [Unit 7 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/7#!cheatsheet).
</details>
