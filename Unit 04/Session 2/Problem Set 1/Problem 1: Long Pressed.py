# Run-time: O(n)
# Space-time: O(1)
def is_long_pressed(name, typed):
    firstPtr = 0 # index exclusively for name string
    secondPtr = 0 # index exclusively for typed string
    # currLetter = name[0] #character
    
    while secondPtr < len(typed):
        # we're looking at the same letter at the same index
        if firstPtr < len(name) and name[firstPtr] == typed[secondPtr]:
            firstPtr += 1
            secondPtr +=1
        
        # long press of the previous name character is the same. (increment secondPtr)
        elif firstPtr > 0 and name[firstPtr - 1] == typed[secondPtr]:
            secondPtr += 1
            
        # else
        else:
            return False
    
    return firstPtr == len(name)

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
