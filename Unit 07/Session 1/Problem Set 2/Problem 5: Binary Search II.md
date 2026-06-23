# Problem 5: Binary Search II

Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list.
Given the recursive solution for binary search below, implement an *iterative* (non-recursive) implementation of binary search.


Evaluate the time and space complexity of your implementation.


```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds

		# find middle index of list
    mid = (left + right) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
	pass
```

Example Usage:


```python
# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
```

Example Output:


```python
# Expected Output: 5
# Explanation: 11 has index 5 in the list
```


### ✨ AI Hint: Binary Search


*Key Skill: Use AI to explain code concepts*


This problem requires you to understand the binary search algorithm. To learn more about this topic, check out the Binary Search section of the [Unit 7 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/7#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the binary search algorithm. Try asking it to explain the concept first, using a real-world analogy. Once you understand the concepts, you can ask it to help you understand how to implement it in Python.
