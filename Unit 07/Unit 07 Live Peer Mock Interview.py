# Link - https://docs.google.com/document/d/1DELfT4BUrHmGiQtt8dG2_RRrhjHXFQTuhVqSWRmIzZQ/edit?tab=t.utap0l1qb8ob

'''
Problem #1 - Find the Index of the First Occurrence in a String
Write a function that, when given two strings, needle and haystack, returns the index of the first occurrence of needle in haystack, or returns -1 if needle is not part of haystack.
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Input: haystack = "leetcode", needle = "leeto"
Output: -1
'''

'''
Understand: 
input: 2 strings. one is bigger than the other
output: an integer: returns the first occurance happens, -1 if i cant find it
edge cases: either or both of the input strings are 0. the needle is for some reason bigger than the haystack. 

Plan:
2 pointer - sliding window
string iterator to slice part of the string, ill move to the end of that string
for loop through haystack
'''

def haystack_needle(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    if len(needle) > len(haystack):
        return -1
    
    hLen = len(haystack)
    nLen = len(needle)
    
    for i in range(0, hLen - nLen + 1):
        if haystack[i:i+nLen] == needle:
            return i
    
    return -1

haystack1 = "sadbutsad"
needle1 = "sad"
print(haystack_needle(haystack1, needle1))

haystack2 = "leetcode"
needle2 = "leeto"
print(haystack_needle(haystack2, needle2))