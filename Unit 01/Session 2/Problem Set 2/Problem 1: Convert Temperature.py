def convertTemp(celsius):
    pass

temperatures = convertTemp(23.00)
print(temperatures)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - celsius is 0")
print("  expected:", [273.15, 32.0], "| got:", convertTemp(0))

print("Test 2 - celsius is 100 (boiling point)")
print("  expected:", [373.15, 212.0], "| got:", convertTemp(100))

print("Test 3 - matches example")
print("  expected:", [296.15, 73.4], "| got:", convertTemp(23.00))

print("Test 4 - decimal celsius value")
print("  expected:", [309.75, 97.88], "| got:", convertTemp(36.6))
