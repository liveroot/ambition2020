array = [9, 2, 3, 2, 6, 6]
result = 9


# Using hash map - dictionary
def find_first_unique_2(arr):
    element_count = {}

    for x in arr:
        element_count[x] = 0

    for x in arr:
        element_count[x] = element_count.get(x) + 1

    for x in arr:
        if element_count.get(x) is 1:
            return x

    return None


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(find_first_unique_2(array)))


if __name__ == '__main__':
    main()
