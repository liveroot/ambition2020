array = [9, 2, 3, 2, 6, 6]
result = 9


# using brute force - nested loop
def find_first_unique_1(arr):
    for x in range(0, len(arr)):
        is_unique = True
        for y in range(0, len(arr)):
            if x is not y and arr[x] is arr[y]:
                is_unique = False
                break

        if is_unique:
            return arr[x]

    return None


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(find_first_unique_1(array)))


if __name__ == '__main__':
    main()
