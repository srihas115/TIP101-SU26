'''
==============================================================================
  Unit 4: Two Pointer & Big O  ·  Session 2  ·  Version 1
  Problem 1: Long Pressed

  Write a function `is_long_pressed()` that takes in a string `name` and a
  string `typed` as parameters. Imagine your friend is typing their `name`
  into a keyboard and when typing a character, the key might get **long
  pressed** and the character will be typed 1 or more times.

  The function should examine the `typed` characters and return `True` if it
  is possible that it was your friends name with some characters being long
  pressed and `False` otherwise.

  Use the **two-pointer approach** to solve the problem, which is a common
  technique in which we initialize two variables (also called a pointer in
  this context) to track different indices or places in a list or string,
  then moves the pointers to point at new indices based on certain
  conditions. A common variation of this technique is to point one variable
  at the beginning of one string and a second pointer at the beginning of a
  second string, then increment each pointer conditionally to solve a
  problem.

  Write your solution for `is_long_pressed` in the space below,
  then click  ▶ Run  to grade it.
  (The full problem, with examples, is in the problem set.)

  ⚠️  Keep the function name `is_long_pressed` and its parameters exactly as given —
      the problem set solution validator looks for that exact name.
==============================================================================
Understand (input, output, core logic): 

Match:

Plan:

'''


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


'''
==============================================================================
  PROBLEM SET SOLUTION VALIDATOR   ·   DO NOT EDIT OR MOVE THIS SECTION
==============================================================================
'''
import sys, pathlib
for _p in pathlib.Path(__file__).resolve().parents:
    if (_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]").is_dir():
        sys.path.insert(0, str(_p / "ProblemSetSolutionValidator[DO_NOT_EDIT]")); break
from problem_set_solution_validator import grade, test

grade(is_long_pressed)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test('alex', 'aaleex', expected=True)   # checks the value your code returns against this example
