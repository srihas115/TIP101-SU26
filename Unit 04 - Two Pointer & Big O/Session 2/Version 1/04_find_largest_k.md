# Problem 4: Positive Negative Pairs

Write a function `find_largest_k()` that takes in a list of integers `nums` that does not contain any zeroes as a parameter. The function finds the **largest positive** integer `k` such that `-k` also exists in the array and returns `k`. If there is no such integer, return `-1`.


```python
def find_largest_k(nums):
    pass
```

Example Usage:


```python
nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))
```

Example Output:


```python
3
-1
```
