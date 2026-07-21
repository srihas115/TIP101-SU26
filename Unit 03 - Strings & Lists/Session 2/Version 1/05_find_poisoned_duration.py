def find_poisoned_duration(time_series, duration):
    pass

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty time_series")
print("  expected:", 0, "| got:", find_poisoned_duration([], 3))

print("Test 2 - single attack")
print("  expected:", 3, "| got:", find_poisoned_duration([5], 3))

print("Test 3 - non-overlapping attacks (no reset needed)")
print("  expected:", 6, "| got:", find_poisoned_duration([1, 10], 3))

print("Test 4 - overlapping attacks, matches the walkthrough in the spec")
print("  expected:", 5, "| got:", find_poisoned_duration([1, 4], 3))
