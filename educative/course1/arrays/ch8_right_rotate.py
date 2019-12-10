array = [1, 2, 3, 4, 5]
result = [5, 1, 2, 3, 4]


def right_rotate(arr):
    temp = arr[len(arr)-1]

    index_list = range(len(arr))

    for i in index_list[::-1]:
        arr[i] = arr[i-1]

    arr[0] = temp

    return arr


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(right_rotate(array)))


if __name__ == '__main__':
    main()
