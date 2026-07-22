# Problem 5: Binary Search I

Binary search is a searching algorithm that allows us to efficiently find the index of a given value within a sorted list.
Given the pseudo code for binary search below, implement an *iterative* (non-recursive) implementation of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!


Evaluate the time and space complexity of your implementation.


```python
def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
		
		# If the value at the middle index is the target value:
			# Return the middle index
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

def binary_search(lst, target):
	pass
```

Example Usage:


```python
# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
```

Example Output:


```
# Expected Output: 5
# Explanation: 11 has index 5 in the list
```


<details>
  <summary>✨ <b>AI Hint: Binary Search</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


This problem requires you to understand the binary search algorithm. To learn more about this topic, check out the Binary Search section of the [Unit 7 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/7#!cheatsheet).


For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the binary search algorithm. Try asking it to explain the concept first, using a real-world analogy. Once you understand the concepts, you can ask it to help you understand how to implement it in Python.
</details>
