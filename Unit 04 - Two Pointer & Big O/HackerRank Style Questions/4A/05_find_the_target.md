# Find the Target

Source: HackerRank Style Unit 4 Assessment, Version A

## Question

You are given a string s consisting of numerical characters and a target sum target. Write a function to
find if there is a pair of adjacent numbers in the string that add up to target. The function should return a
boolean value: True if such a pair exists, and False otherwise.
Use the two-pointer technique to solve this problem without converting the entire string into a list of
numbers.
Note: Each character in the string s should be treated as a separate digit; for example, '56' in the string
should be considered as '5' and '6'.

Example 1:
Input: s = "1234", target = 5
Output: True
Explanation: The digits '2' and '3' are adjacent and add up to 5.
Example 2:
Input: s = "1112", target = 4
Output: False
Explanation: There are no two adjacent digits that add up to 4.
