import educative.course1.stacks_queues.stack as s


# Implementation uses 2 stacks, one for storing the queue elements,
# and 2nd as a buffer to be used at the time of dequeue
# 1. Enqueue simply pushes the value on top of stack 1
# 2. Dequeue checks if stack 1 and stack 2 are empty and returns False if no elements
# 3. IF stack 2 is empty, stack 1 is emptied into stack 2
# 4. This operation reverses the order of stored elements
#    and the top element in stack 2 represents the front of the queue
# 5. Elements in stack 2 can be pooped for dequeuing until it goes empty.
# 6. and IF stack2 is NOT emptied yet, it still contains the front element in the queue.
# 7. Finally, result is popped off of stack 2 and returned to the caller
class QueueUsingStacks_2:
    def __init__(self, capacity=None, suppress_printing=False):
        self.suppress_printing = suppress_printing
        self.capacity = capacity
        self.stack1 = s.Stack(self.capacity, suppress_printing)
        self.stack2 = s.Stack(self.capacity, suppress_printing)

    def is_empty(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            return True
        return False

    def is_full(self):
        if self.stack1.is_full() or self.stack2.is_full():
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("nothing to show, queue empty...")
            return None
        elif self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

            result = self.stack2.peek()
        else:
            result = self.stack2.peek()

        return result

    def enqueue(self, data):
        if self.is_full():
            print("can't enqueue anymore, queue full...")
            return False

        self.stack1.push(data)
        if not self.suppress_printing: print("enqueued data = " + str(data))

        return True

    def dequeue(self):
        if self.is_empty():
            print("can't dequeue, queue empty...")
            return None
        elif self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

            result = self.stack2.pop()
        else:
            result = self.stack2.pop()

        if not self.suppress_printing: print("dequeued data = " + str(result))
        return result

    def print_queue(self):
        pretty_queue = self.prettify()
        print(pretty_queue)

    def prettify(self):
        printer = "Queue -> F [ "
        for x in self.stack1.elements:
            printer += str(x) + " "
        printer += "] B"

        return printer
