import educative.course1.stacks_queues.ch2_two_stacks as two_stacks


def main():
    print("Stack initialized with capacity = 5")
    example = two_stacks.TwoStacks(5, True) # suppress_printing = True

    print("------")
    print("pushing to stack 1...")
    example.push1(5)
    example.push1(6)
    example.push1(7)
    print("pushing to stack 2...")
    example.push2(8)
    example.push2(9)
    example.push2(2)
    example.push2(7)

    print()
    print("peeking from stack 1...")
    print(example.peek1())

    print()
    print("peeking from stack 2...")
    print(example.peek2())

    print()
    example.print_stack()

    print("------")
    print("popping from stack 1..")
    example.pop1()
    print("popping from stack 2..")
    example.pop2()

    print()
    print("peeking from stack 1...")
    print(example.peek1())

    print()
    print("peeking from stack 2...")
    print(example.peek2())

    print()
    example.print_stack()

    print("------")
    print("popping from stack 1..")
    example.pop1()
    example.pop1()
    print("popping from stack 2..")
    example.pop2()
    example.pop2()
    example.pop2()

    print()
    print("peeking from stack 1...")
    print(example.peek1())

    print()
    print("peeking from stack 2...")
    print(example.peek2())

    print()
    example.print_stack()

    print("------")
    print("pushing to stack 2...")
    example.push2(21)
    example.push2(22)
    example.push2(23)

    print()
    print("peeking from stack 1...")
    print(example.peek1())

    print()
    print("peeking from stack 2...")
    print(example.peek2())

    print()
    example.print_stack()


if __name__ == '__main__':
    main()
