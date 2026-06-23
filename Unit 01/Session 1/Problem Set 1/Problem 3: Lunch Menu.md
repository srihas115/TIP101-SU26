# Problem 3: Lunch Menu

The following function accepts one parameter `menu`. Copy this code into your IDE and add a function call so that `"Lunch today is: 🍕"` is printed to the console.


```python
def print_menu(menu):
    print("Lunch today is: " + menu)
```

Example Output: `Lunch today is: 🍕`


### 💡 Hint: Parameters


The variable listed between the () of a function defintion is known as a parameter. They act as placeholders for the values (also known as an argument) that you will pass to the function when you call it. Parameters allow functions to accept input and operate on it, making functions more flexible and reusable. The argument is the value of a parameter


```python
def greeting(name):
    print("Hello " + name)

student1 = "Marc"
greeting(student1) # Prints to the console: Hello Marc
greeting("Alexandra") # Prints to the console: Hello Alexandra
```

In the above example, name is the parameter within the function definition. In the first instance of calling greeting, we pass in student1, a variable that holds a string value. In the second instance, we directly pass the string "Alexandra" as the argument to the function, demonstrating that arguments can either be variables or direct values.


### ✨ AI Hint: Parameters, Arguments, and Variables Oh My!


*Key Skill: Use AI to explain code concepts*


The difference between parameters, arguments, and variables is subtle, and you will likely hear them used interchangeably much of the time. For the first few hints, we gave you a detailed breakdown of the concept right here in the course portal! However, a critical part of becoming a software engineer is learning to teach yourself new concepts.


To flex your research skills, try asking a generative AI tool like ChatGPT or GitHub Copilot to explain the difference between parameters, arguments, and variables. You can ask it for a simple comparison table, or code examples to illustrate the differences.
