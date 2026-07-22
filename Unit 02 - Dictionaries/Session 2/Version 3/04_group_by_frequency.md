# Problem 4: Group By Frequency

Write a function `group_by_frequency()` that takes in a list `lst` and returns a dictionary where keys represent the frequency of unique elements within `lst` and values represent a list of elements with the same frequency.


```python
def group_by_frequency(lst):
    pass
```

Example Usage:


```python
lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))
```

Example Output:


```
{ 1 : ['a', 'b'], 2: ['c', 'd'], 3: ['e']}
```


<details>
  <summary>✨ <b>AI Hint: Frequency Maps</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


A dictionary that maps unique values to their frequencies within a given data structure or data type is often called a **frequency map**. Frequency maps are an extremely useful problem solving tool that you will see often throughout this unit and in future units.


We encourage you to learn by doing and attempt this problem before doing a deeper dive! However, if you get stuck, you can ask a generative AI tool like ChatGPT or GitHub Copilot to explain the concept.


For example, you could say:


*"You're an expert computer science tutor for a Python-based technical interviewing course. Please explain what a frequency map is, and provide one or more examples of simple technical interview problems in which a frequency map is useful."*
</details>
