# Problem 3: Evaluate Two Sum

The `two_sum()` problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.


Then, evaluate the time and space complexity of the following solution:


```python
def two_sum(nums, target):
    prev_map = {}  # Value to index mapping

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[nums[i]] = i
```

Which has better time complexity?

Which has better space complexity?


<details>
  <summary>💡 <b>Hint: Big O (Time & Space Complexity)</b></summary>

  <br>

Big O notation is a mathematical notation in computer science used to describe the the time and space complexity of an algorithm. Time complexity is the amount of time an algorithm or function takes to run in comparison to the size of the input data. Space complexity is the amount of extra memory or space an algorithm or function needs to complete its task in comparison to the size of the input data.


For your convenience, we've included a summary of the three most common Big O functions below.


Common Big O includes:


- **O(1) - Constant Time** No matter the size of your input data, the function takes a fixed amount of time or memory to complete its task.

Example: Summing two numbers

```python
def sum(a, b):
 return a + b
```

It takes the computer roughly the same amount of time to sum `a` and `b` no matter how large the two numbers are.

- **O(n) - Linear Time** The amount of time or memory your function needs grows linearly with the size of your input data.

Example: Printing each item in a list

```python
def print_list(lst):
 for item in lst:
 print(item)
```

The computer has to perform one extra print statement for each extra item there is in the list, so the length of time it takes to print the list will be proportional to the number of items in the list. We expect that it will take 1000 times longer to print a list with 1000 elements than it will to print a list with just 1 element.

- **O(n²) - Quadratic Time** The amount of time or memory your function needs grows quadratically with the size of your input data.

Example: Finding Duplicates Using a Nested For Loop

```python
def find_duplicates(lst):
 n = len(lst)
 for i in range(n):
 for j in range(i + 1, n):
 if lst[i] == lst[j]:
 print(f"Duplicate found: {lst[i]}")
 return True
 return False
```

The function compares each element in the list to every other element in the list, which means we perform roughly n² comparisons where n is the length of our input list `lst`, so it will take n² time to complete all comparisons. We can expect that for a list of size 2, we will perform roughly 4 comparisons whereas for a list of size 10 we will perform roughly 100 comparisons.
</details>
<details>
  <summary>✨ <b>AI Hint: Decoding Big O</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


Big O is a big topic, and kind of tricky to wrap your head around! If you're feeling confused, try asking an AI tool like ChatGPT or GitHub Copilot to explain it to you:


*"You're an expert computer science tutor for a Python-based technical interviewing prep course. Can you use an analogy to help me understand Big O notation? Please explain the concept of time and space complexity in a way that is easy to understand."*


Once it gives you an answer, you can ask follow-up questions to clarify any points that are still confusing. Be patient with yourself, and remember that this is a complex topic that takes time to fully understand!
</details>
