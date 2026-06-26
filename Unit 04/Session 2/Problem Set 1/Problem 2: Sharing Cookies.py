# Run-time: O(n)
# Space-time: O(1)
def find_content_children(s, g):
    
    child = 0 # pointer index for child
    cookie = 0 # pointer index for cookie

    while child < len(g) and cookie < len(g):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
               
    
    return child

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

print(find_content_children(s, g))
# Output: 2


g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

print(find_content_children(s, g))
# Output: 2