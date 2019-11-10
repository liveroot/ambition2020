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

    def insert_at_head(self, data):
        if self.is_empty():
            self.head = Node()
            self.head.value = data
            return

        new = Node()
        new.value = data
        new.prev = None
        new.next = self.head

        if self.head is not None:
            self.head.prev = new

        self.head = new

    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        new = Node()
        new.value = data
        new.next = None

        current = self.head
        while current.next is not None:
            current = current.next

        new.prev = current
        current.next = new

    def insert_after(self, after, data):
        if self.is_empty():
            print("list is empty")
            return None

        new = Node()
        new.value = data

        current = self.head
        while current.next is not None and current.value is not after:
            current = current.next

        if current is None:
            print("value not found")
            return

        new.prev = current
        new.next = current.next
        current.next = new

        def print_list(self):
            if self.is_empty():
                print("list is empty")
                return

            current = self.head
            while current.next is not None:
                print(current.value)
                current = current.next

            print(current.value)
