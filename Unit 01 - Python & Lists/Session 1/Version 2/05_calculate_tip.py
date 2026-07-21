def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return .1 * bill
    elif service_quality == "average":
        return .15 * bill
    elif service_quality == "excellent":
        return .2 * bill
    else:
        return None

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - bill=0, poor service (zero tip)")
print("  expected:", 0.0, "| got:", calculate_tip(0, "poor"))

print("Test 2 - bill=100, excellent service")
print("  expected:", 20.0, "| got:", calculate_tip(100, "excellent"))

print("Test 3 - unrecognized service_quality string")
print("  expected:", None, "| got:", calculate_tip(50, "great"))

print("Test 4 - negative bill, poor service")
print("  expected:", -5.0, "| got:", calculate_tip(-50, "poor"))

print("Test 5 - case-sensitive mismatch ('Poor' vs 'poor')")
print("  expected:", None, "| got:", calculate_tip(50, "Poor"))

print("Test 6 - empty string service_quality")
print("  expected:", None, "| got:", calculate_tip(50, ""))
