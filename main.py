import MapCharToInt


def section2(list):
    for i in range(len(list)):
        list[i] -= 3 * i
    return list


if __name__ == '__main__':
    a = MapCharToInt.MapCharToInt('Hello DS').get()
    print(a)

    b = section2(a)
    print(b)

