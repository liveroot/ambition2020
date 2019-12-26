class Stack:
    def __init__(self, capacity=None, suppress_printing=False):
        self.suppress_printing = suppress_printing
        self.capacity = capacity
        self.top = -1
        self.elements = [None] * self.capacity

    def is_empty(self):
        if self.top is -1:
            return True
        return False

    def is_full(self):
        if self.top is (self.capacity - 1):
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("nothing to show, stack empty...")
            return None

        return self.elements[self.top]

    def push(self, data):
        if self.is_full():
            print("can't push anymore, stack full...")
            return None

        self.top += 1
        self.elements[self.top] = data
        if not self.suppress_printing: print("pushed data = " + str(data))

    def pop(self):
        if self.is_empty():
            print("can't pop, stack empty...")
            return None

        result = self.elements[self.top]
        self.elements[self.top] = None
        self.top -= 1

        if not self.suppress_printing: print("popped data = " + str(result))
        return result

    def print_stack(self):
        pretty_list = self.prettify()
        print(pretty_list)

    def prettify(self):
        printer = ""
        for i in range(len(self.elements))[::-1]:
            printer += (str(i) + " -> " + "[ " + str(self.elements[i]) + " ]")
            if i is not 0: printer += "\n"
        return printer
