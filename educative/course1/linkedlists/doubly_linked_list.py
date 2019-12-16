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

        self.head.prev = new
        self.head = new

    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        current = self.head
        while current.next is not None:
            current = current.next

        new = Node()
        new.value = data
        new.next = None

        current.next = new
        new.prev = current

    def insert_after(self, after, data):
        if self.is_empty():
            return

        current = self.head
        while current.next is not None and current.value is not after:
            current = current.next

        if current is None:
            print("can't insert, value not found")
            return

        new = Node()
        new.value = data
        new.prev = current
        new.next = current.next
        if current.next is not None:
            current.next.prev = new
        current.next = new

    def search_node(self, data):
        if self.is_empty():
            return False

        current = self.head
        while current.next is not None:
            if current.value is data:
                return True
            current = current.next

        return False

    def delete_at_head(self):
        if self.is_empty():
            return

        current = self.head
        self.head = current.next
        self.head.prev = None

    def delete_at_end(self):
        if self.is_empty():
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.prev.next = None

    def delete_by_value(self, data):
        if self.is_empty():
            return

        current = self.head

        if current.value is data:
            self.delete_at_head()
            return

        while current.next is not None:
            if current.value is data:
                current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next

        print("can't delete, value not found")

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return

        pretty_list = self.prettify()
        print(pretty_list)

    def prettify(self):
        start_tag = "[H] None"
        end_tag = "None"
        printer = ""

        printer += start_tag
        printer += ' <- '

        current = self.head
        while current is not None:
            printer += str(current.value)
            current = current.next

            if current:
                printer += " <-> "
            else:
                printer += " -> "

        printer += end_tag

        return printer
