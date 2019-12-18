import educative.course1.stacks_queues.stack as stack


def main():
    print("Stack initialized with capacity = 5")
    example = stack.Stack(5)

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
    example.print_stack()

    print("------")
    print("peeking at the top...")
    print(example.peek())

    print("------")
    print("popping from stack..")
    example.pop()
    example.pop()

    print()
    example.print_stack()

    print("------")
    print("peeking at the top...")
    print(example.peek())

    print("------")
    print("popping from stack..")
    example.pop()
    example.pop()
    example.pop()
    example.pop()
    example.pop()

    print()
    example.print_stack()

    print("------")
    print("peeking at the top...")
    print(example.peek())

    print("------")
    print("pushing to stack...")
    example.push(21)
    example.push(22)

    print()
    example.print_stack()

    print("------")
    print("peeking at the top...")
    print(example.peek())


if __name__ == '__main__':
    main()
