# Problem 5: Product of Two Integers

Write a function `product()` that returns the product of two integers, `a` and `b`.


Example Input: `22` and `7`

Example Result: `154`


### ✨ AI Hint: To Print or to Return?


*Key Skill: Use AI to explain code concepts*


To print or to return? That is the question.


This problem requires you to know the difference between printing (`print()` in Python) and returning a value inside of a function. If you're unfamiliar with the differences, you can ask an AI tool like ChatGPT or GitHub Copilot to explain it to you.


### 💡 Hint: Print vs. Return Examples


Note that `print()` is often used in conjunction with a function that returns a value. For example, below we have a function `return_param()` below which simply returns whatever argument is given to it.


```python
def return_param(my_param):
    return my_param
```

We can return then call our function and store it in a variable:


```python
result = return_param("I am the return value!")
```

Then print the returned value to the console:


```python
print(result) # Prints "I am the return value!" to the console.
```

To shorten the above two lines into a single line of code, we can call our function directly within our print statement.


Python will first evaluate the expression or function call within the parentheses of our print statement `return_param("I am the return value!")`. The function call will evaluate to its return value, the string `"I am the return value!"`, and then that string becomes the argument to our print function call.


```python
print(return_param("I am the return value!"))
```

To take a closer look at this example, try testing it out in [Python Tutor](https://pythontutor.com/render.html#code=def%20return_param%28my_param%29%3A%0A%20%20%20%20return%20my_param%0A%20%20%20%20%0A%20%20%20%20%0Aprint%28return_param%28%22I%20am%20the%20return%20value!%22%29%29&cumulative=false&curInstr=5&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) or looking at Example 6 in the `Print` section of the [Unit 1 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/1#!cheatsheet)!
