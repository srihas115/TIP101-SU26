def return_book(title, library):
    pass

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty library, add new book")
print("  expected:", {"New Book": 1}, "| got:", return_book("New Book", {}))

print("Test 2 - book exists, increments quantity")
print("  expected:", {"X": 6}, "| got:", return_book("X", {"X": 5}))

print("Test 3 - single key-value pair, book not present")
print("  expected:", {"Y": 3, "Z": 1}, "| got:", return_book("Z", {"Y": 3}))
