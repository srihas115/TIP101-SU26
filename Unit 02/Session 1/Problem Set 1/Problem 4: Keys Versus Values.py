def keys_v_values(dictionary):
    pass

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dictionary (both sums are 0)")
print("  expected:", "balanced", "| got:", keys_v_values({}))

print("Test 2 - single key-value pair, equal key and value")
print("  expected:", "balanced", "| got:", keys_v_values({5: 5}))

print("Test 3 - keys sum greater than values sum")
print("  expected:", "keys", "| got:", keys_v_values({10: 1, 20: 2}))

print("Test 4 - values sum greater than keys sum")
print("  expected:", "values", "| got:", keys_v_values({1: 10, 2: 20}))

print("Test 5 - negative numbers, keys sum greater than values sum")
print("  expected:", "keys", "| got:", keys_v_values({-1: -5}))

print("Test 6 - all values equal across multiple keys, sums balanced")
print("  expected:", "balanced", "| got:", keys_v_values({1: 2, 2: 1}))
