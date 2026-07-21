def dict_difference(d1, d2):
    pass

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.
# Note: per the problem prose, dict_difference(first, second) returns pairs found in
# `first` that are not matching pairs in `second`. These tests call it in that natural
# (non-swapped) order to keep the expected values unambiguous.

print("Test 1 - both dicts empty")
print("  expected:", {}, "| got:", dict_difference({}, {}))

print("Test 2 - second dict empty (all of first dict is unique)")
print("  expected:", {"a": 1}, "| got:", dict_difference({"a": 1}, {}))

print("Test 3 - some keys shared with matching values (excluded), one unique")
print("  expected:", {"b": 2}, "| got:", dict_difference({"a": 1, "b": 2}, {"a": 1}))

print("Test 4 - key present in both but with different value (included)")
print("  expected:", {"x": 5}, "| got:", dict_difference({"x": 5}, {"x": 9}))
