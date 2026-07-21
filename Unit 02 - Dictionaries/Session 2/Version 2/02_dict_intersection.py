def dict_intersection(d1, d2):
    pass

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
print(dict_intersection(d1, d2))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty dicts")
print("  expected:", {}, "| got:", dict_intersection({}, {}))

print("Test 2 - no matching key-value pairs")
print("  expected:", {}, "| got:", dict_intersection({"a":1}, {"a":2}))

print("Test 3 - all pairs match")
print("  expected:", {"x":1,"y":2}, "| got:", dict_intersection({"x":1,"y":2}, {"x":1,"y":2}))

print("Test 4 - key present in both but with different values (excluded)")
print("  expected:", {}, "| got:", dict_intersection({"k":1}, {"k":2}))
