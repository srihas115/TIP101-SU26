def compress_string(my_str):
    pass

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single character (compression not smaller, unchanged)")
print("  expected:", "a", "| got:", compress_string("a"))

print("Test 2 - all-same-character string (compression is smaller)")
print("  expected:", "a4", "| got:", compress_string("aaaa"))

print("Test 3 - empty string")
print("  expected:", "", "| got:", compress_string(""))
