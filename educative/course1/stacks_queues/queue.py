class Queue:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.elements = []
        self.current_size = 0

    def is_empty(self):
        if self.current_size is 0:
            return True
        return False

    def is_full(self):
        if self.current_size is self.capacity:
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("nothing to show, queue empty...")
            return None

        return str(self.elements[0])

    def enqueue(self, data):
        if self.is_full():
            print("can't enqueue anymore, queue full...")
            return None

        self.elements.append(data)
        self.current_size = len(self.elements)
        print("enqueued data = " + str(data))

    def dequeue(self):
        if self.is_empty():
            print("can't dequeue, queue empty...")
            return None

        result = self.elements.pop(0)
        self.current_size = len(self.elements)
        print("dequeued data = " + str(result))

        return result

    def print_queue(self):
        pretty_queue = self.prettify()
        print(pretty_queue)

    def prettify(self):
        printer = "Queue -> F [ "
        for x in self.elements:
            printer += str(x) + " "
        printer += "] B"

        return printer
