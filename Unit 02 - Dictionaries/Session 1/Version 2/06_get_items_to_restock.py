def get_items_to_restock(products, restock_threshold):
    pass

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty products dictionary")
print("  expected:", [], "| got:", get_items_to_restock({}, 5))

print("Test 2 - all quantities below threshold")
print("  expected:", ["Product1", "Product2"], "| got:", get_items_to_restock({"Product1": 1, "Product2": 2}, 5))

print("Test 3 - all quantities equal to threshold (not restocked, since it must be strictly less)")
print("  expected:", [], "| got:", get_items_to_restock({"Product1": 5, "Product2": 5}, 5))

print("Test 4 - all quantities above threshold")
print("  expected:", [], "| got:", get_items_to_restock({"Product1": 10, "Product2": 20}, 5))

print("Test 5 - threshold of 0 (nothing needs restocking)")
print("  expected:", [], "| got:", get_items_to_restock({"Product1": 3, "Product2": 0}, 0))

print("Test 6 - single product below threshold")
print("  expected:", ["Product1"], "| got:", get_items_to_restock({"Product1": 1}, 5))
