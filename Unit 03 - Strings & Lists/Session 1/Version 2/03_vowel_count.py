def vowel_count(s):
    pass

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - empty string")
print("  expected:", 0, "| got:", vowel_count(""))

print("Test 2 - single vowel character")
print("  expected:", 1, "| got:", vowel_count("e"))

print("Test 3 - single consonant character")
print("  expected:", 0, "| got:", vowel_count("b"))

print("Test 4 - all-same-character string, all vowels")
print("  expected:", 4, "| got:", vowel_count("aaaa"))

print("Test 5 - mixed case vowels")
print("  expected:", 5, "| got:", vowel_count("AEIOU"))

print("Test 6 - punctuation and whitespace mixed in")
print("  expected:", 3, "| got:", vowel_count("a! e? i."))
