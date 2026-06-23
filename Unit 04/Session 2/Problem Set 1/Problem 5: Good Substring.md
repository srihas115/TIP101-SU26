# Problem 5: Good Substring

The **sliding window technique** is an algorithmic technique often used to find a subarray or substring that meets certain criteria. It works by initializing two pointers to point at the start and end of a ‘window’ or subsection of the string/array at a time. The pointers are then incremented to slide the window and examine a different subarray or substring.


Use the sliding window technique to solve the following problem:


Write a function `count_good_substrings()` that takes in a string `s` as a parameter and returns the number of **good substrings** of length three. A string is good if there are no repeated characters. A substring is a continuous sequence of characters in a string.

If there are multiple occurrences of the same substring, every occurrence should be counted.


```python
def count_good_substrings(s):
    pass
```

Example Usage:


```python
s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))
```


```python
1
4
```


<details>
  <summary>💡 <b>Hint: Sliding Window Technique</b></summary>

  <br>

This problem may require the use of the sliding window technique, an extension of the two-pointer technique. For an in-depth review of the sliding window technique, check out the [Unit 4 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/4#!cheatsheet).
</details>
