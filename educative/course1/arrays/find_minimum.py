array = [9, 2, 3, 6]
result = 2


def find_minimum(arr):
    min_value = arr[0]
    for x in arr:
        if x < min_value:
            min_value = x

    return min_value


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(find_minimum(array)))


if __name__ == '__main__':
    main()
