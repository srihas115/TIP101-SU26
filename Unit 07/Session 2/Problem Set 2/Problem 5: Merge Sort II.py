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

# Example Input:  left = [1,3,5], right = [2,4]
