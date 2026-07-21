def student_directory(student_names):
    res = {}
    
    for i in range(len(student_names)):
        res[student_names[i]] = i + 1
    
    return res

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - example from spec")
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print("  expected:", {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 5}, "| got:", student_directory(student_names))

print("Test 2 - empty list of student names")
print("  expected:", {}, "| got:", student_directory([]))

print("Test 3 - single student")
print("  expected:", {"Grace Hopper": 1}, "| got:", student_directory(["Grace Hopper"]))

print("Test 4 - duplicate student name (later occurrence overwrites the ID for that key)")
print("  expected:", {"Ada": 3, "Bo": 2}, "| got:", student_directory(["Ada", "Bo", "Ada"]))
