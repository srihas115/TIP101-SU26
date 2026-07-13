class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
    pass

# 1 -> 0 -> 1
num3 = Node(1)
num2 = Node(0, num3)
num1 = Node(1, num2)   # head of the list

int_num = binary_to_int(num1)
# 101 in binary is 5
print(int_num)  # Output: 5

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node list, value 1")
single_one = Node(1)
print("  expected:", 1, "| got:", binary_to_int(single_one))

print("Test 2 - single-node list, value 0")
single_zero = Node(0)
print("  expected:", 0, "| got:", binary_to_int(single_zero))

print("Test 3 - longer binary number (1101 = 13)")
b4 = Node(1)
b3 = Node(0, b4)
b2 = Node(1, b3)
b1 = Node(1, b2)
print("  expected:", 13, "| got:", binary_to_int(b1))
