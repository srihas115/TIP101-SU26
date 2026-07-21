def common_keys(dict1, dict2):
    pass

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dicts")
print("  expected:", [], "| got:", common_keys({}, {}))

print("Test 2 - no common keys")
print("  expected:", [], "| got:", common_keys({"a":1}, {"b":2}))

print("Test 3 - all keys common")
print("  expected:", ["x","y"], "| got:", common_keys({"x":1,"y":2}, {"x":9,"y":9}))

print("Test 4 - one dict is empty")
print("  expected:", [], "| got:", common_keys({"a":1}, {}))
