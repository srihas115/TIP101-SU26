def sum_of_number_strings(nums):
    pass

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty list")
print("  expected:", 0, "| got:", sum_of_number_strings([]))

print("Test 2 - single-element list")
print("  expected:", 7, "| got:", sum_of_number_strings(["7"]))

print("Test 3 - negative number strings")
print("  expected:", 5, "| got:", sum_of_number_strings(["-5", "10"]))

print("Test 4 - list containing a zero string")
print("  expected:", 10, "| got:", sum_of_number_strings(["0", "10"]))
