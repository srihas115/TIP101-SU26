def team_with_best_average_score(games):
    pass

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers",
     "score": 30
    },
    {"team_name": "Lions",
     "score": 27
    },
    {"team_name": "Bears",
     "score": 20
    },
    {"team_name": "Tigers",
     "score": 24
    },
    {"team_name": "Bears",
     "score": 22
    }
]

print(team_with_best_average_score(games))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single game, single team")
print("  expected:", "Lions", "| got:", team_with_best_average_score([{"team_name": "Lions", "score": 10}]))

print("Test 2 - two teams, clear winner")
print("  expected:", "Bears", "| got:", team_with_best_average_score([
    {"team_name": "Lions", "score": 5},
    {"team_name": "Bears", "score": 50}
]))

print("Test 3 - winner determined by average, not a single high score")
print("  expected:", "Wolves", "| got:", team_with_best_average_score([
    {"team_name": "Foxes", "score": 100},
    {"team_name": "Foxes", "score": 0},
    {"team_name": "Wolves", "score": 60},
    {"team_name": "Wolves", "score": 60}
]))
