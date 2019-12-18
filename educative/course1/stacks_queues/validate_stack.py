import educative.course1.stacks_queues.stack as stack


def main():
    example = stack.Stack(5)

    # pushing elements to stack
    print("pushing to stack")
    example.push(5)
    example.push(6)
    example.push(7)
    example.push(8)
    example.push(9)
    example.push(2)
    example.print_stack()

    # popping elements from stack
    print("popping data..")
    print(example.pop())
    example.print_stack()

    # peeking from the stack
    print("peeking at the top..")
    print(str(example.peek()))
    example.print_stack()


if __name__ == '__main__':
    main()
