class TwoStacks():
    def __init__(self, capacity=None, suppress_printing=False):
        self.suppress_printing = suppress_printing
        self.capacity = capacity
        self.elements = [None] * self.capacity
        self.top1 = -1
        self.top2 = self.capacity

    def is_full(self):
        if abs(self.top1 - self.top2) is 1:
            return True
        return False

    def is_empty(self):
        if self.top1 is -1 and self.top2 is self.capacity:
            return True
        return False

    def push1(self, data):
        if self.is_full():
            print("can't push anymore, stack full...")
            return None

        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.elements[self.top1] = data
            if not self.suppress_printing: print("stack1 - pushed data = " + str(data))
        return None

    def push2(self, data):
        if self.is_full():
            print("can't push anymore, stack full...")
            return None

        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.elements[self.top2] = data
            if not self.suppress_printing: print("stack2 - pushed data = " + str(data))
        return None

    def pop1(self):
        if self.is_empty():
            print("can't pop, stack empty...")
            return None

        if self.top1 > -1:
            result = self.elements[self.top1]
            self.elements[self.top1] = None
            self.top1 -= 1
            if not self.suppress_printing: print("stack1 - popped data = " + str(result))
            return result
        return None

    def pop2(self):
        if self.is_empty():
            print("can't pop, stack empty...")
            return None

        if self.top2 < self.capacity:
            result = self.elements[self.top2]
            self.elements[self.top2] = None
            self.top2 += 1
            if not self.suppress_printing: print("stack2 - popped data = " + str(result))
            return result
        return None

    def peek1(self):
        if self.top1 is -1:
            return None
        return str(self.elements[self.top1])

    def peek2(self):
        if self.top2 is self.capacity:
            return None
        return str(self.elements[self.top2])

    def print_stack(self):
        pretty_list = self.prettify()
        print(pretty_list)

        return None

    def prettify(self):
        printer = ""
        for i in range(self.capacity):
            printer += str(i) + " -> [  " + str(self.elements[i]) + "  ]"
            if i is not self.capacity: printer += "\n"

        return printer
