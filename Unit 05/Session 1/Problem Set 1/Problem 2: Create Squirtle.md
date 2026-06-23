# Problem 2: Create Squirtle

Step 1: Add the `print_pokemon` definition below to your code on your IDE.


Step 2: Instantiate an instance of the class `Pokemon` and store it in a variable named `squirtle`. The Pokemon instance created should have `name` "Squirtle" and its `types` should be ["Water"].


Step 3: Call the method `print_pokemon()` on your new Pokemon instance `squirtle`.


```python
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })
```

Example Usage:


```python
squirtle = Pokemon("Squirtle", ["water"])
squirtle.print_pokemon()
```

Example Output:


```python
{'name': 'Squirtle', 'types': ['water'], 'is_caught': False}
```


<details>
  <summary>✨ <b>AI Hint: Class Methods</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This question requires you to be familiar with class methods, which are functions attached to an object. To help, we've included more info [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)


If you'd still like to see more examples or ask follow-up questions, try using an AI tool like ChatGPT or GitHub Copilot. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Please provide 2-3 examples of how Class Methods are used in Python, and explain how each one works."*


You might also want to ask questions like:


*"Can you explain the difference between class methods, instance methods, and functions?"*
</details>
