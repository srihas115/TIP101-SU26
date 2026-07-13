def build_inventory(product_names, product_prices):
    pass

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty lists")
print("  expected:", {}, "| got:", build_inventory([], []))

print("Test 2 - single-element lists")
print("  expected:", {"Mango": 1.5}, "| got:", build_inventory(["Mango"], [1.5]))

print("Test 3 - duplicate prices across products")
print("  expected:", {"A": 1.0, "B": 1.0}, "| got:", build_inventory(["A","B"], [1.0,1.0]))

print("Test 4 - zero price")
print("  expected:", {"Free Sample": 0.0}, "| got:", build_inventory(["Free Sample"], [0.0]))
