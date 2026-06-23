# Problem 5: Merge Sort II

Merge sort is a sorting algorithm that takes in an unsorted list and returns a sorted list in `O(n log n)` time which is faster than many other sorting algorithms that have `O(n²)` time complexity. It uses a divide and conquer approach.


Merge sort works by using a divide and conquer approach: it divides the array into two halves until each sublist contains only a single element, then it recursively sorts each sublist, and merges the sorted sublists into a sorted array.


Given the main function `merge_sort()` below, implement the helper function `merge()` below. `merge()` accepts two sorted lists `left` and `right` and returns a sorted list.


```python
def merge_sort(lst):
		# If the length of the list is 0-1, the list is already sorted.
    if len(lst) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2
    # Divide the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted arrays
    return merge(left_half, right_half)

def merge(left, right):
	pass
```

Example Usage:


```python
# Example Input:  left = [1,3,5], right = [2,4]
```

Example Output:


```python
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
