import educative.course1.stacks_queues.ch10_min_stack as min_stack


def main():
    print("Stack initialized with capacity = 5")
    example = min_stack.MinStack(6)

    print("------")
    print("pushing to stack...")
    example.push(5)
    example.push(6)
    example.push(7)
    example.push(8)
    example.push(9)
    example.push(2)
    example.push(7)

    print()
    print("peeking from stack...")
    print(example.peek())

    print()
    example.print_stack()

    print("------")
    print("popping from stack..")
    example.pop()
    example.pop()

    print()
    print(example.peek())

    print()
    example.print_stack()

    print("------")
    print("popping from stack..")
    example.pop()
    example.pop()
    example.pop()
    example.pop()
    example.pop()

    print()
    print("peeking from stack...")
    print(example.peek())

    print()
    example.print_stack()

    print("------")
    print("pushing to stack...")
    example.push(7)
    example.print_stack()
    example.print_min_stack()
    print("minimum: " + str(example.min()))

    print()
    print("pushing to stack...")
    example.push(8)
    example.print_stack()
    example.print_min_stack()
    print("minimum: " + str(example.min()))

    print()
    print("pushing to stack...")
    example.push(5)
    example.print_stack()
    example.print_min_stack()
    print("minimum: " + str(example.min()))

    print()
    print("pushing to stack...")
    example.push(9)
    example.print_stack()
    example.print_min_stack()
    print("minimum: " + str(example.min()))

    print()
    print("pushing to stack...")
    example.push(5)
    example.print_stack()
    example.print_min_stack()
    print("minimum: " + str(example.min()))

    print()
    print("pushing to stack...")
    example.push(2)
    example.print_stack()
    example.print_min_stack()
    print("minimum: " + str(example.min()))


if __name__ == '__main__':
    main()
