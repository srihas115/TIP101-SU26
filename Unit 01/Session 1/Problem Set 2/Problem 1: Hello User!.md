# Problem 1: Hello User!

Write a function `greet_user()` that takes in a string `name` as a parameter and prints `"Hello <name>"`.


```python
def greet_user(name):
    pass
```

Example Input: `Michael`

Example Output: `Hello Michael`


*Note: `pass` is a keyword that is used as a placeholder for future code*


<details>
  <summary>💡 <b>Hint: Python Functions</b></summary>

  <br>

In Python, functions are defined using the `def` keyword.


A function is a block of organized, reusable code that is used to perform a single, related action. In Python we write simple functions using the following syntax:


Example Usage:


```python
# Example: Function that prints Hello world!
def function_example():
  print("Hello world!")
```
</details>

Functions can be called by writing the function name followed by parentheses.


Example Usage:


```python
# Example: Calling a function
function_example() # Prints 'Hello world!'
```


<details>
  <summary>💡 <b>Hint: Parameters</b></summary>

  <br>

The variable listed between the () of a function defintion is known as a parameter. They act as placeholders for the values (also known as an argument) that you will pass to the function when you call it. Parameters allow functions to accept input and operate on it, making functions more flexible and reusable. The argument is the value of a parameter


```python
def greeting(name):
    print("Hello " + name)

student1 = "Marc"
greeting(student1) # Prints to the console: Hello Marc
greeting("Alexandra") # Prints to the console: Hello Alexandra
```

In the above example, name is the parameter within the function definition. In the first instance of calling greeting, we pass in student1, a variable that holds a string value. In the second instance, we directly pass the string "Alexandra" as the argument to the function, demonstrating that arguments can either be variables or direct values.
</details>
<details>
  <summary>✨ <b>AI Hint: Parameters, Arguments, and Variables Oh My!</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


The difference between parameters, arguments, and variables is subtle, and you will likely hear them used interchangeably much of the time. For the first few hints, we gave you a detailed breakdown of the concept right here in the course portal! However, a critical part of becoming a software engineer is learning to teach yourself new concepts.


To flex your research skills, try asking a generative AI tool like ChatGPT or GitHub Copilot to explain the difference between parameters, arguments, and variables. You can ask it for a simple comparison table, or code examples to illustrate the differences.
</details>
