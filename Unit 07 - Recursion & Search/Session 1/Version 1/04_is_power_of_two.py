'''
1. understand
    input: n
    output: return True if n is a power of two
    core logic: recursion

3. plan
    edge case: handle if n is negative
        then its false, because n can never be negative regardless of what x (such that n == 2^x)
    base case: n == 1, because that happens when n == 1 == 2^0. we reached a whole number
    recursive case: recurse on n divided by 2 rounded down (to account for float)
'''

# Time: O(log(n))
# Space: O(log(n))
def is_power_of_two(n):
    if n <= 0: # edge case if n is negative
        return False
    if n == 1: # base case, we reached a whole number
        return True
    if n % 2 != 0: # base case, we reached a odd number
        return False
    
    return is_power_of_two(n // 2)

def is_power_of_three(n):
    if n <= 0: # edge case if n is negative
        return False
    if n == 1: # base case, we reached a whole number
        return True
    if n % 3 != 0: # base case, we reached a odd number
        return False
    
    return is_power_of_three(n // 3)


print(is_power_of_two(16))
print(is_power_of_two(18))
print(is_power_of_two(1))
print(is_power_of_two(3))

# n = 2^x

# 2.0 == 2 -> true
# type(2.0) == type(2) -> false
# print(4 / 2)
# print(4 // 2)

# print(0.1 + 0.2)