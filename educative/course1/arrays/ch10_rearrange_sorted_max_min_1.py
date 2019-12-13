array = [1,2,3,4,5]
result = [5,1,4,2,3]


# using 2 pointers and a switch variable
def rearrange_sorted_max_min_1(arr):
    switch = False
    front = 0
    rear = len(arr) - 1
    temp = [0 for x in arr]

    for i in range(len(arr)):
        if switch is False:
            temp[i] = arr[rear]
            rear -= 1
        else:
            temp[i] = arr[front]
            front += 1
        switch = not switch

    for i in range(len(arr)):
        arr[i] = temp[i]

    return arr


def main():
    print("Input: " + str(array))
    print("Expected: " + str(result))
    print("Output: " + str(rearrange_sorted_max_min_1(array)))


if __name__ == '__main__':
    main()
