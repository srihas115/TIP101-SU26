class SLLNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class DLLNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

def dll_to_sll(dll_head):
    pass

# DLL: Ice <-> Water <-> Steam
Steam = DLLNode("Steam")
Water = DLLNode("Water", Steam)
Ice = DLLNode("Ice", Water)
Steam.prev = Water
Water.prev = Ice
dll_head = Ice
sll_head = dll_to_sll(dll_head)

#SLL: Ice -> Water -> Steam

def _to_list(head):
    vals = []
    while head is not None:
        vals.append(head.value)
        head = head.next
    return vals

print(_to_list(sll_head))

# ==== AI-generated test cases (added by Claude via Claude Code) ====
# These are AI-generated edge-case tests, not part of the original CodePath problem set.
# They check correctness beyond the single example call above.

print("Test 1 - single-node DLL")
single_dll = DLLNode("Solo")
result1 = dll_to_sll(single_dll)
print("  expected:", ["Solo"], "| got:", _to_list(result1))

print("Test 2 - empty DLL (head is None)")
result2 = dll_to_sll(None)
print("  expected:", None, "| got:", result2)

print("Test 3 - DLL with duplicate values")
dup_c = DLLNode("X")
dup_b = DLLNode("X", dup_c)
dup_a = DLLNode("X", dup_b)
dup_c.prev = dup_b
dup_b.prev = dup_a
result3 = dll_to_sll(dup_a)
print("  expected:", ["X", "X", "X"], "| got:", _to_list(result3))
