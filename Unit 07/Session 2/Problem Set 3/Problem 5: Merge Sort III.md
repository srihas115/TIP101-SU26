# Problem 5: Merge Sort III

Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in `O(n log n)` time which is faster than many other sorting algorithms that have `O(n²)` time complexity. It uses a divide and conquer approach.


Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.


Given the pseudo-code below, implement the `merge_sort()` function.


```python
def merge(left, right):
	# Initialize an empty list to store the merged result
	# Initialize a pointer to iterate over the left input list
	# Initialize a pointer to iterate over the right input list
	
	# Iterate over left & right lists simultaneously
		# Compare elements at same indices of left and right halves of the list
		# Add them to the result list in the correct order
  # Add any remaining elements from the left half to the result list
  # Add any remaining elements from the right half to the result list

def merge_sort(lst):
    pass
```

Example Usage:


```python
# Example Input: [5,3,4,2,1]
```

Example Output:


```python
# Expected Output: [1,2,3,4,5]
```


### ✨ AI Hint: Divide and Conquer


*Key Skill: Use AI to explain code concepts*


Merge sort (and binary search!) are examples of algorithms that use the divide and conquer technique. To learn more about this topic, check out the Divide and Conquer and Merge Sort sections of the [Unit 7 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/7#!cheatsheet).


If you have more questions, try asking an AI tool like ChatGPT or GitHub Copilot to explain the divide and conquer technique.


You can ask it to provide a real-world analogy to help you understand the concept better. Once you grasp the idea, you can ask it to help you implement a divide and conquer algorithm in Python, such as merge sort or binary search.
