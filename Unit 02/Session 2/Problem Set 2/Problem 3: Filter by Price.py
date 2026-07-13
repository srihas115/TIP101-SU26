def remove_items_below_price(items, price_threshold):
    pass

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dict")
print("  expected:", None, "| got:", remove_items_below_price({}, 1.00))

print("Test 2 - threshold so low nothing is removed")
print("  expected:", None, "| got:", remove_items_below_price({"apple": 1.99}, 0.01))

print("Test 3 - threshold removes every item")
print("  expected:", ["apple", "banana"], "| got:", remove_items_below_price({"apple": 1.00, "banana": 2.00}, 5.00))

print("Test 4 - single item removed")
print("  expected:", ["cheap"], "| got:", remove_items_below_price({"cheap": 0.50, "pricey": 9.99}, 1.00))
