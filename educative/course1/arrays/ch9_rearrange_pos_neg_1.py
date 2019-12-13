array = [10, -1, 20, 4, 5, -9, -6]
result = [-1, -9, -6, 10, 20, 4, 5]


# using temp array and overwrite on orig
def rearrange_pos_neg_1(arr):
    temp = []
    for x in arr:
        if x < 0:
            temp.append(x)

    for x in arr:
        if x >= 0:
            temp.append(x)

    for y in range(len(temp)):
        arr[y] = temp[y]

    return arr


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(rearrange_pos_neg_1(array)))


if __name__ == '__main__':
    main()
