def restock_inventory(current_inventory, restock_list):
    for k, v in restock_list.items():
        current_inventory[k] = current_inventory.get(k, 0) + v
    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty restock list (inventory unchanged)")
print("  expected:", {"apples": 30, "bananas": 15}, "| got:", restock_inventory({"apples": 30, "bananas": 15}, {}))

print("Test 2 - empty current inventory (all items new)")
print("  expected:", {"apples": 10, "pears": 5}, "| got:", restock_inventory({}, {"apples": 10, "pears": 5}))

print("Test 3 - restock item not in current inventory")
print("  expected:", {"apples": 30, "kiwis": 8}, "| got:", restock_inventory({"apples": 30}, {"kiwis": 8}))

print("Test 4 - restock quantity of 0 (item stays the same)")
print("  expected:", {"apples": 30}, "| got:", restock_inventory({"apples": 30}, {"apples": 0}))

print("Test 5 - both dictionaries empty")
print("  expected:", {}, "| got:", restock_inventory({}, {}))

print("Test 6 - multiple new items added at once")
print("  expected:", {"apples": 30, "kiwis": 4, "mangoes": 2}, "| got:", restock_inventory({"apples": 30}, {"kiwis": 4, "mangoes": 2}))