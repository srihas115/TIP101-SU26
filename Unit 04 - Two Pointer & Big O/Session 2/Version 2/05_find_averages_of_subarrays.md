# Problem 5: Averages of Subarray

The **sliding window technique** is an algorithmic technique often used to find a subarray or substring that meets certain criteria. It works by initializing two pointers to point at the start and end of a ‘window’ or subsection of the string/array at a time. The pointers are then incremented to slide the window and examine a different subarray or substring.


Use the sliding window technique to solve the following problem:


Write a function `find_averages_of_subarrays()` that takes in a list of integers `nums` and an integer `k` as parameters. The function returns a list where each element in the average of each contiguous subarray of size `k` in `nums` where `1 ≤k ≤ len(nums)`


```python
def find_averages_of_subarrays(k, nums):
	pass
```

Example Usage:


```python
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
avg_lst = find_averages_of_subarrays(5, nums)
```

Example Output:


```
[2.2, 2.8, 2.4, 3.6, 2.8]
# (1 + 3 + 2 + 6 - 1)/5 = 2.2
# (3 + 2 + 6 -1 + 4)/5 = 2.8
# ... and so forth
```


<details>
  <summary>💡 <b>Hint: Sliding Window Technique</b></summary>

  <br>

This problem may require the use of the sliding window technique, an extension of the two-pointer technique. For an in-depth review of the sliding window technique, check out the [Unit 4 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/4#!cheatsheet).
</details>
