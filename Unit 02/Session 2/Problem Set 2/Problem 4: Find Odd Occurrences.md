# Problem 4: Find Odd Occurrences

Write a function `find_odd_occurrences()` that takes in a list of integers `numbers` where all numbers occur an even number of times except for two unique numbers that occur an odd number of times. The function should find the two unique numbers and return them as a list. Assume each problem has exactly one solution.


```python
def find_odd_occurrences(numbers):
    pass
```

Example Usage:


```python
numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)
```

Example Output:


```python
[1,3]
```


### ✨ AI Hint: Frequency Maps


*Key Skill: Use AI to explain code concepts*


A dictionary that maps unique values to their frequencies within a given data structure or data type is often called a **frequency map**. Frequency maps are an extremely useful problem solving tool that you will see often throughout this unit and in future units.


We encourage you to learn by doing and attempt this problem before doing a deeper dive! However, if you get stuck, you can ask a generative AI tool like ChatGPT or GitHub Copilot to explain the concept.


For example, you could say:


*"You're an expert computer science tutor for a Python-based technical interviewing course. Please explain what a frequency map is, and provide one or more examples of simple technical interview problems in which a frequency map is useful."*
