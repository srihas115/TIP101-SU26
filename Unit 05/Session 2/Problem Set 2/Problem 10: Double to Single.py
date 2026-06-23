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
dll_head = Ice
sll_head = dll_to_sll(dll_head)

#SLL: Ice -> Water -> Steam
