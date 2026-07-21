# Problem 4: Binary Substrings

Write a function `binary_substrings_count()` that takes in a string `s` representing a binary number as a parameter. The function counts the number of substrings that satisfy all of the following conditions:


- contains an equal number of `0`s and `1`s

- all the `0`s in the substring are grouped consecutively

- all the `1`s in the substrings are grouped consecutively


```python
def binary_substrings_count(s):
    pass
```

Example Usage:


```python
s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))
```

Example Output:


```python
# substrings for s: "0011", "01", "1100", "10", "0011", "01"
6
# substrings for s2: "10", "01", "10", "01"
4
# substrings for s3:
0
```
