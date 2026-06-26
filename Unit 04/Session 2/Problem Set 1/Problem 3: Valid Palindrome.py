# using iterators
def valid_palindrome1(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            # return the check of the skipped character
            skip_left = s[start+1 : end+1]
            skip_right = s[start : end]
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
        start += 1
        end -= 1
    return True



# Using helper method
def valid_palindrome2(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return is_valid_palindrome_HELPER(s, start+1, end) or is_valid_palindrome_HELPER(s, start, end-1)
        start += 1
        end -= 1
    return True

# helper for valid_palindrome2(s)
def is_valid_palindrome_HELPER(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1 
    return True
    

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome1(s))
print(valid_palindrome1(s2))
print(valid_palindrome1(s3))

print()

print(valid_palindrome2(s))
print(valid_palindrome2(s2))
print(valid_palindrome2(s3))
