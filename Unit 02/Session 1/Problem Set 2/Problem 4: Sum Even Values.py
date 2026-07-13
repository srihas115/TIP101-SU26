def sum_even_values(dictionary):
    pass

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dictionary")
print("  expected:", 0, "| got:", sum_even_values({}))

print("Test 2 - all odd values")
print("  expected:", 0, "| got:", sum_even_values({"a": 1, "b": 3, "c": 5}))

print("Test 3 - all even values")
print("  expected:", 12, "| got:", sum_even_values({"a": 2, "b": 4, "c": 6}))

print("Test 4 - includes a zero value (0 is even)")
print("  expected:", 6, "| got:", sum_even_values({"a": 0, "b": 6, "c": 1}))

print("Test 5 - includes negative even values")
print("  expected:", -2, "| got:", sum_even_values({"a": -4, "b": 1, "c": 2}))

print("Test 6 - single key-value pair, even value")
print("  expected:", 10, "| got:", sum_even_values({"a": 10}))
