class MathOperation:
    def AbsoluteValue(self,arr):
        for i in range(len(arr)):
            arr[i] = abs(arr[i])

        return arr

    # part 2
    def functionX(self,list):
        for i in range(len(list)):
            list[i] -= 3 * i
        return list