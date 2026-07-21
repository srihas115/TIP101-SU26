'''

3. plan
    ((())) --> empty
    (

    

'''

def is_nested(s):
    if s == "":
        return True
    if s[0] == "(" and s[-1] == ")":
        return is_nested(s[1:-1])
    return False

# Example Input: "(())"
example = "(())"
print(is_nested(example))