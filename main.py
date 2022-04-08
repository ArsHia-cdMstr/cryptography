from IntToChar import intToChar
from MapCharToInt import MapCharToInt
from part2 import section2
from part5 import AbsoluteValue
from placement import placement
from sort import sort, bubbleSort
from ui import ui


def processing(filename):
    file_r = open(filename, "r")  # read

    a = MapCharToInt(file_r.read()).get()
    print(a)

    b = section2(a)
    print(b)

    c = sort(b)
    print(c)

    d = bubbleSort(c)
    print(d)

    e = AbsoluteValue(d)
    print(e)

    f = placement(e)
    print(f)

    g = intToChar(f)
    print(g)

    file_w = open('file_w.txt', "w")  # write
    file_w.write(str(g))

    return g


if __name__ == '__main__':
    ui()
