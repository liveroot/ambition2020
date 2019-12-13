array = [10, -1, 20, 4, 5, -9, -6]
result = [-1, -9, -6, 10, 20, 4, 5]


# in-place swaps
def rearrange_pos_neg_2(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            if i is not j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
    return arr


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(rearrange_pos_neg_2(array)))


if __name__ == '__main__':
    main()
