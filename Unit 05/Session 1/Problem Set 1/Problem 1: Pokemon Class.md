# Problem 1: Pokemon Class

Step 1: Copy the following code into your IDE.


Step 2: Add a line of code (outside of the class) to instantiate an instance of the class `Pokemon` and store it in a variable named `my_pokemon`. The Pokemon instance created should have `name` `"Pikachu"` and its `types` should be `["Electric"]`.


```python
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
```


<details>
  <summary>✨ <b>AI Hint: Intro to Object Oriented Programming</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem may require you to be familiar with Object Oriented Programming (OOP) basics, including classes, instances, objects, and constructors. To help, we've included an "intro to OOP" review [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/5#!cheatsheet)


You can also use an AI tool like ChatGPT or GitHub Copilot to get more examples or ask follow-up questions. You can use the following prompt as a starting point:


*"You're an expert computer science tutor. Can you help me understand OOP conceptually, using analogies to real-world objects?"*


Once you understand the concept, you can also ask follow-up questions like:


*"Can you provide an example of a class, instance, and constructor in python?"*


*"What does `self` mean in Python, and how is it used in OOP?"*
</details>
