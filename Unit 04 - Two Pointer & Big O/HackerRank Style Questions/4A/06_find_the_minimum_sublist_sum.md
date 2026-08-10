# Find the Minimum Sublist Sum

Source: HackerRank Style Unit 4 Assessment, Version A

## Question

Given a list of integers nums and an integer k, write a function to find the minimum sum of any
contiguous sublist of size k. If the size of nums is less than k, return 0.

Example 1:
Input: nums = [5, -1, 3, 2, -4], k = 2
Output:  -2
Explanation: Explanation: The sublist of length 2 are [5, -1], [-1, 3], [3, 2], and [2, -4].
Their sums are 4, 2, 5, and -2 respectively. The smallest sum among these is -2, which comes from
the sublist [2, -4].
Example 2:
Input: nums[4,2,-5,1,3], k =1
Output: -5
Explanation: Here the sublist is just one element, smallest element is -5.
