def calculate_gpa(report_card):
    pass

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single course, grade A")
print("  expected:", 4.0, "| got:", calculate_gpa({"Math": "A"}))

print("Test 2 - all F grades")
print("  expected:", 0.0, "| got:", calculate_gpa({"Math": "F", "Science": "F"}))

print("Test 3 - one of each grade letter (A,B,C,D)")
print("  expected:", 2.5, "| got:", calculate_gpa({"Math": "A", "Science": "B", "History": "C", "Art": "D"}))

print("Test 4 - all grades equal (B, B)")
print("  expected:", 3.0, "| got:", calculate_gpa({"Math": "B", "Science": "B"}))

print("Test 5 - empty report card (edge case: no courses, would divide by zero)")
print("  expected printed output: 0.0, or a ZeroDivisionError depending on how the empty case is handled")
try:
    print("  got:", calculate_gpa({}))
except ZeroDivisionError:
    print("  got: ZeroDivisionError raised")
