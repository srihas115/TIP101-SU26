# Problem 5: Merge Sort I

Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in `O(n log n)` time which is faster than many other sorting algorithms that have `O(n²)` time complexity. It uses a divide and conquer approach.


Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.


Given the pseudo-code and helper function `merge()` below, implement the `merge_sort()` function.


```python
# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
	result = [] # List to store the merged result
	i = j = 0 # Pointers to iterate over left and right input arrays
	
	# Compare elements from left and right halves of the list and add them to the
	# result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1

  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1

  return result

def merge_sort(lst):
	pass
```

Example Usage:


```python
# Example Input: [5,3,4,2,1]
```

Example Output:


```
# Expected Output: [1,2,3,4,5]
```


<details>
  <summary>✨ <b>AI Hint: Divide and Conquer</b></summary>

  <br>

*Key Skill: Use AI to explain code concepts*


Merge sort (and binary search!) are examples of algorithms that use the divide and conquer technique. To learn more about this topic, check out the Divide and Conquer and Merge Sort sections of the [Unit 7 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/7#!cheatsheet).


If you have more questions, try asking an AI tool like ChatGPT or GitHub Copilot to explain the divide and conquer technique.


You can ask it to provide a real-world analogy to help you understand the concept better. Once you grasp the idea, you can ask it to help you implement a divide and conquer algorithm in Python, such as merge sort or binary search.
</details>
