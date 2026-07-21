def swap_ends(my_str):
    pass

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single character string (first and last are the same char)")
print("  expected:", "a", "| got:", swap_ends("a"))

print("Test 2 - empty string")
print("  expected:", "", "| got:", swap_ends(""))

print("Test 3 - two character string")
print("  expected:", "ba", "| got:", swap_ends("ab"))

print("Test 4 - all-same-character string")
print("  expected:", "zzzz", "| got:", swap_ends("zzzz"))

print("Test 5 - mixed case string")
print("  expected:", "eodC", "| got:", swap_ends("CodE"))

print("Test 6 - string with punctuation/whitespace ends")
print("  expected:", " hi!", "| got:", swap_ends("! hi "))
