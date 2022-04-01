# part 3
def sort(arr):
    comparingNum = 0;
    for i in range(len(arr)):

        if (arr[comparingNum] > 0):
            if (arr[i] < 0):
                # swap
                temp = arr[comparingNum]
                arr[comparingNum] = arr[i]
                arr[i] = temp

                comparingNum += 1

        else:
            comparingNum += 1

    return arr


# part 4
def bubbleSort(arr):
    for i in range(len(arr)):

        swapped = False

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                swapped = True

        if not swapped:
            break

    return arr