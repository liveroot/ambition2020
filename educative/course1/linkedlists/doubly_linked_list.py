class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if self.head is None:
            return True
