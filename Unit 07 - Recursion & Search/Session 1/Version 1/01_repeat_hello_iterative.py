# Time: O(n)
# Space: O(n)
def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)

print("Recursive")
repeat_hello(5)

# Time: O(n)
# Space: O(1)
def repeat_hello_iterative(n):
    for i in range(n):
        print("Hello")

print("Iterative")     
repeat_hello_iterative(5)