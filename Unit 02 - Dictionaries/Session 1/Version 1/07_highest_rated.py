def highest_rated(books):
    if len(books) == 0:
        return None
    
    highest_rated = books[0]
    for book in books:
        if book.get("rating", 0) > highest_rated.get("rating", 0):
            highest_rated = book
    return highest_rated

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

# ==== AI-generated test cases (added by Copilot) ====
print("Test 1 - example from spec")
print("  expected:", {"title": "A Fortune For Your Disaster", "author": "Hanif Abdurraqib", "rating": 4.47}, "| got:", highest_rated(books))

print("Test 2 - empty list")
print("  expected:", None, "| got:", highest_rated([]))

print("Test 3 - tie ratings (first highest returned)")
books_tie = [
    {"title": "Book A", "author": "X", "rating": 4.5},
    {"title": "Book B", "author": "Y", "rating": 4.5}
]
print("  expected:", {"title": "Book A", "author": "X", "rating": 4.5}, "| got:", highest_rated(books_tie))

print("Test 4 - missing rating field (treated as 0)")
books_missing = [
    {"title": "No Rating", "author": "Anon"},
    {"title": "Has Rating", "author": "A", "rating": 3.5}
]
print("  expected:", {"title": "Has Rating", "author": "A", "rating": 3.5}, "| got:", highest_rated(books_missing))


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

grade(highest_rated)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([{'title': 'T1', 'author': 'Zevin', 'rating': 4.18}, {'title': 'T2', 'author': 'Abdurraqib', 'rating': 4.47}, {'title': 'T3', 'author': 'Reid', 'rating': 4.4}], expected={'title': 'T2', 'author': 'Abdurraqib', 'rating': 4.47})   # checks the value your code returns against this example
