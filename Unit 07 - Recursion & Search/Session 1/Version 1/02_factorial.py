# Time: O(n) because n recursive calls before hitting the base case
# Space: O(n) because n stack frames alive simultaneously since each call is waiting on n * factorial(n-1) to return before it can multiply and return itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))
# Example Input: 5
