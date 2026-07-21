# Problem 2: Two-Pointer Reverse List

Write a function `reverse_list()` that takes in a list `lst` and returns elements of the list in reverse order. The list should be reversed *in-place* without using list slicing (e.g. `lst[::-1]`).


Instead, use the **two-pointer approach**, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.


```python
def reverse_list(lst):
    pass
```

Example Input: `[1, 2, 3, 4, 5]`

Example Output: `[5, 4, 3, 2, 1]`


<details>
  <summary>💡 <b>Hint: Two Pointer Technique</b></summary>

  <br>

This problem requires the use of the two pointer technique. For a more in-depth review of the two-pointer technique, check out the [Unit 4 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/4#!cheatsheet), specifically the opposite direction variation.
</details>
