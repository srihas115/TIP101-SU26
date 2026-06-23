# Problem 1: Mountain Peak

A mountain list is defined as a list that has at least three elements, where there exists some `i` with `0 < i < len(lst)-1` such that `lst[0] < lst[1] < ... lst[i-1] < lst[i]` and `lst[i] > lst[i+1] > ... > lst[len(lst)-1]`.


Given such a mountain list `lst` as a parameter, write a function that finds and returns the highest peak (the index `i` of the maximum element).


```python
def peak_index_in_mountain_list(lst):
    pass
```

Example Usage:


```python
mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)
```

Example Output: `2`


<details>
  <summary>💡 <b>Hint: Problem Type</b></summary>

  <br>

As a review from the previous unit, this question is a lists question! You do not need to know anything about dictionaries to solve this problem.
</details>
