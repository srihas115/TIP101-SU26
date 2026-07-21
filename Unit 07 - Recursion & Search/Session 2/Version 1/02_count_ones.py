'''
plan
    
'''


def count_ones_iterative(lst):
    left = 0
    right = len(lst) - 1
    first_1 = len(lst)

    while left <= right:
        middle = left + (right - left) // 2
        if lst[middle] == 1:
            first_1 = middle
            right = middle - 1
        else:
            left = middle + 1

    return len(lst) - first_1

def count_ones_recursive(lst, left=0, right=None):
    if right is None:
        right = len(lst) - 1

    if left > right:
        return 0  # no 1s found in this range

    middle = (left + right) // 2

    if lst[middle] == 1:
        # count 1s to the left of (and including) mid, plus everything right of mid
        return count_ones_recursive(lst, left, middle - 1) + (right - middle + 1)
    else:
        return count_ones_recursive(lst, middle + 1, right)

# Example Input: [0, 0, 0, 0, 1, 1, 1]
print(count_ones_iterative([0, 0, 0, 0, 1, 1, 1]))
print(count_ones_recursive([0, 0, 0, 0, 1, 1, 1]))