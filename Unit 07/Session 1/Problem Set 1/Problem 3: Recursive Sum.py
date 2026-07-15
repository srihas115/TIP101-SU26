'''
1. understand
    input: list
    output: sum of all values
    core logic: recursion

3. plan
    base case: if the list is empty, then return 0
    recursive step:
        return the value of the first element of the list + sum_list(rest of the list)


'''

# Time: O(n^2) because because each of the n calls creates a new slice lst[1:],
#       and slicing a list of length k takes O(k) time to copy — summing
#       n + (n-1) + ... + 1 gives O(n^2) total work.
# Space: O(n^2) because each call also holds a newly allocated slice in
#        memory until its call returns (sizes n-1, n-2, ..., 0), in addition
#        to the O(n) call stack — the slice copies dominate the total.
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

# Time: O(n) because i indexes into lst and increments once per call, and
#       lst[i] is an O(1) lookup with no copying — n calls, O(1) work each.
# Space: O(n) because the call stack grows one frame per call until the
#        base case is hit, but no extra lists are ever created — just n
#        stacked frames, each holding a reference to the same lst and an int.
def sum_list2(lst, i=0):                    # pass in a default parameter
    if len(lst) == i:
        return 0
    return lst[i] + sum_list2(lst, i + 1)   # no list iterators, slicing via indexes

# Example Input: [1, 2, 3, 4, 5]
print(sum_list([1,2,3,4,5]))
print(sum_list([5]))
print(sum_list([]))

print()

# No list iterators
print(sum_list2([1,2,3,4,5]))
print(sum_list2([5]))
print(sum_list2([]))