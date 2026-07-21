# Problem 2: Checking Subsequence

Write a function `is_subsequence` that takes in two strings `s` and `t` as parameters and returns `True` if `s` is a subsequence of `t` and `False` otherwise.


A **subsequence** of a string is a new string that is formed from the original string by deleting some or none of the characters without disturbing the relative positions of the remaining characters. (*i.e., "ace" is a subsequence of "abcde" while "aec" is not*).


```python
def is_subsequence(s, t):
	pass
```

Example Usage:


```python
s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))
```

Example Output:


```python
True
False
```


<details>
  <summary>💡 <b>Hint: Two Pointer Technique, Same Direction Variation</b></summary>

  <br>

This problem may require the use of the two pointer technique. For a more in-depth review of the two-pointer technique, check out the [Unit 4 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/4#!cheatsheet), specifically the same direction variation.
</details>
