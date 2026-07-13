def find_unique_items(list_a, list_b):
    pass

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - matches example")
print("  expected:", {"carrot": True, "date": False}, "| got:", find_unique_items(["apple","banana","carrot"], ["apple","banana","date"]))

print("Test 2 - identical lists (no unique items)")
print("  expected:", {}, "| got:", find_unique_items(["a","b"], ["a","b"]))

print("Test 3 - completely disjoint lists")
print("  expected:", {"x": True, "y": False}, "| got:", find_unique_items(["x"], ["y"]))

print("Test 4 - empty lists")
print("  expected:", {}, "| got:", find_unique_items([], []))

print("Test 5 - list_a empty, list_b has items")
print("  expected:", {"z": False}, "| got:", find_unique_items([], ["z"]))
