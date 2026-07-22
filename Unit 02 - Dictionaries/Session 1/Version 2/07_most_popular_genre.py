def most_popular_genre(movies):
    pass

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix",
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice",
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility",
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single movie")
print("  expected:", "Comedy", "| got:", most_popular_genre([{"title": "Airplane!", "genre": "Comedy", "rating": 7.9}]))

print("Test 2 - multiple movies in the same genre (average of the two)")
print("  expected:", "Horror", "| got:", most_popular_genre([
    {"title": "A", "genre": "Horror", "rating": 6.0},
    {"title": "B", "genre": "Horror", "rating": 8.0}
]))

print("Test 3 - clear winner among three genres")
print("  expected:", "Drama", "| got:", most_popular_genre([
    {"title": "A", "genre": "Drama", "rating": 9.5},
    {"title": "B", "genre": "Comedy", "rating": 6.0},
    {"title": "C", "genre": "Action", "rating": 7.0}
]))

print("Test 4 - empty movies list (edge case, undefined by spec)")
print("  expected printed output: None, or an error/exception, depending on how the empty case is handled")
try:
    print("  got:", most_popular_genre([]))
except (ValueError, ZeroDivisionError) as e:
    print("  got: exception raised:", type(e).__name__)


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

grade(most_popular_genre)   # ▶ Run this file to validate your solution

'''
==============================================================================
  YOUR OWN TEST CASES   ·   optional — uncomment & edit to try your own inputs
==============================================================================
'''
# test([{'title': 'Inception', 'genre': 'Science Fiction', 'rating': 8.8}, {'title': 'The Matrix', 'genre': 'Science Fiction', 'rating': 8.7}, {'title': 'Pride and Prejudice', 'genre': 'Romance', 'rating': 7.8}, {'title': 'Sense and Sensibility', 'genre': 'Romance', 'rating': 7.7}], expected='Science Fiction')   # checks the value your code returns against this example
