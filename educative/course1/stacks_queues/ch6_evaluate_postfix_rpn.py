import educative.course1.stacks_queues.stack as s

input_data = "921*-8-4+"
expected_output_data = 3


# PostFix or RPN notations have the operator between two numbers
# written after the concerned numbers as an epxression (like 912+-4+2* = 20)
# So stacks are perfect to evaluate such strings as you can push the items to
# a stack if they are numerical, otherwise if current character is an operator,
# we pop last two numerical items from the stack and perform the operation
def evaluate_postfix_rpn(expression_string):
    expression = list(expression_string)
    temp_stack = s.Stack(len(expression), True) # suppress_printing = True
    valid_input = ["+", "-", "/", "*"]

    for c in expression:
        if c not in valid_input and not c.isdigit():
            return "Expression is invalid!"

        if c is "+":
            x = int(temp_stack.pop())
            y = int(temp_stack.pop())
            temp_stack.push(y + x)
        elif c is "-":
            x = int(temp_stack.pop())
            y = int(temp_stack.pop())
            temp_stack.push(y - x)
        elif c is "*":
            x = int(temp_stack.pop())
            y = int(temp_stack.pop())
            temp_stack.push(y * x)
        elif c is "/":
            x = int(temp_stack.pop())
            y = int(temp_stack.pop())
            temp_stack.push(y//x)
        else:
            temp_stack.push(c)

    result = temp_stack.pop()

    return result


def main():
    print("Input: " + str(input_data))
    print("Expected: " + str(expected_output_data))
    print("Output: " + str(evaluate_postfix_rpn(input_data)))


if __name__ == '__main__':
    main()
