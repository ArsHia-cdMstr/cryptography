import MapCharToInt
from sort import bubbleSort, sort
from placement import placement
from part5 import AbsoluteValue
from part2 import section2

if __name__ == '__main__':
    file_r = open('file.txt', "r")  # read

    a = MapCharToInt.MapCharToInt(file_r.read()).get()
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

    file_w = open('file_w.txt', "w")  # write
    file_w.write(str(f))
