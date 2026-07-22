# Problem 2: Count Pairs

Write a function `count_pairs()` that takes in a *0-indexed* list of integers `nums` of length `n` and an integer `target` as parameters. The function returns the number of index pairs `(i, j)` where `0 <= i < j < n` and `nums[i] + nums[j] < target`.


```python
def count_pairs(nums, target):
	pass
```

Example Usage:


```python
nums = [-1,1,2,3,1]
print(count_pairs(nums,2))

nums2 = [-6,2,5,-2,-7,-1,3]
print(count_pairs(nums2,2))
```

Example Output:


```
# nums[0] + nums[1] = 0
# nums[0] + nums[2] = 1
# nums[0] + nums[4] = 0
3

# nums[0] + nums[1] = -4
# nums[0] + nums[3] = -8
# nums[0] + nums[4] = -13
# nums[0] + nums[5] = -7
# nums[0] + nums[6] = -3
# nums[1] + nums[4] = -5
# nums[3] + nums[4] = -9
# nums[3] + nums[5] = -3
# nums[4] + nums[5] = -8
# nums[4] + nums[6] = -4
10
```


<details>
  <summary>💡 <b>Hint: Two Pointer Technique, Same Direction Variation</b></summary>

  <br>

This problem may require the use of the two pointer technique. For a more in-depth review of the two-pointer technique, check out the [Unit 4 Cheatsheet](https://courses.codepath.org/courses/tip101/unit/4#!cheatsheet), specifically the same direction variation.
</details>
