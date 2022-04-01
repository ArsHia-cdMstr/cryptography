# part 6
def placement(arr):
    arr_copy = arr.copy()

    length = len(arr_copy)

    for i in range(length):
        arr.insert(2 * i + 1, arr_copy[length - (i + 1)])

    return arr

