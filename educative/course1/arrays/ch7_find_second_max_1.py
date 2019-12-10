array = [9, 2, 3, 6]
result = 6


# traversing array twice
def find_second_max_1(arr):
    maximum = -1
    for x in arr:
        if x > maximum:
            maximum = x

    second_maximum = -1
    for y in arr:
        if second_maximum < y < maximum:
            second_maximum = y

    return second_maximum


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(find_second_max_1(array)))


if __name__ == '__main__':
    main()
