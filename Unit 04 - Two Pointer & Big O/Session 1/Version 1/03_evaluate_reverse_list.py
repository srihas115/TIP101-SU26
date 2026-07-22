'''
==============================================================================
    Unit 4: Two Pointer & Big O  ·  Session 1  ·  Version 1
    Problem 3: Evaluating Solutions
==============================================================================
'''


def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
