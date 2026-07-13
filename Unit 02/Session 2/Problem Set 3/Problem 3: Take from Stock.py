def pop_stock(items, item_name, quantity):
    pass

items = {"chocolate": 20, "candy": 5, "chips": 10}

resultA = pop_stock(items, "candy", 2)
resultB = pop_stock(items, "candy", 5)
resultC = pop_stock(items, "lollipops", 5)
resultD = pop_stock(items, "chocolate", 5)

print(resultA)
print(resultB)
print(resultC)
print(resultD)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - removing exact remaining stock (down to zero)")
print("  expected:", {"candy": 0}, "| got:", pop_stock({"candy": 5}, "candy", 5))

print("Test 2 - item not present")
print("  expected:", "Item does not exist.", "| got:", pop_stock({"candy": 5}, "gum", 1))

print("Test 3 - quantity greater than stock")
print("  expected:", "Not enough stock.", "| got:", pop_stock({"candy": 5}, "candy", 10))

print("Test 4 - removing zero quantity (dict unchanged)")
print("  expected:", {"candy": 5}, "| got:", pop_stock({"candy": 5}, "candy", 0))
