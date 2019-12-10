array = [9, 2, 3, 6]
result = 6


# traversing arrays twice
def find_second_max_2(arr):
    maximum = -1
    second_maximum = -1

    for x in arr:
        if x > maximum:
            second_maximum = maximum
            maximum = x
        elif second_maximum < x < maximum:
            second_maximum = x

    return second_maximum


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(find_second_max_2(array)))


if __name__ == '__main__':
    main()
