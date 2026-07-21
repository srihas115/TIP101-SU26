def odd_keys_even_values(dictionary):
    pass

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dict")
print("  expected:", [], "| got:", odd_keys_even_values({}))

print("Test 2 - all keys even (none qualify)")
print("  expected:", [], "| got:", odd_keys_even_values({2: 4, 4: 8}))

print("Test 3 - odd key but odd value (excluded)")
print("  expected:", [], "| got:", odd_keys_even_values({3: 5}))

print("Test 4 - negative odd key with even value")
print("  expected:", [-3], "| got:", odd_keys_even_values({-3: 2}))

print("Test 5 - single qualifying pair")
print("  expected:", [7], "| got:", odd_keys_even_values({7: 10}))
