class Map:
    def __charToInt(self, char):
        if ord('A') <= ord(char) <= ord('Z'):
            return int(ord(char) - 65)

        if ord('a') <= ord(char) <= ord('z'):
            return int(ord(char) - 71)

        if ord(char) == ord(' '):
            return int(51)

        if ord(char) == ord('\n'):
            return int(52)

        if ord(char) == ord(','):
            return int(53)

        if ord(char) == ord('.'):
            return int(54)

        if ord(char) == ord('?'):
            return int(55)

        if ord(char) == ord('!'):
            return int(56)

    def getInt(self, string):
        arr = list()
        for char in string:
            arr.append(self.__charToInt(char))
        return arr

    # final part
    def __intToChar(self, intNum):

        # upper-case words
        if 0 <= intNum <= 25:
            return chr(intNum + 65)

        # lower-case words
        elif 26 <= intNum <= 50:
            return chr(intNum + 71)

        elif intNum == 51:
            return " "

        elif intNum == 52:
            return "\n"

        elif intNum == 53:
            return ","

        elif intNum == 54:
            return "."

        elif intNum == 55:
            return "?"

        elif intNum == 56:
            return "!"

    def getString(self, array):
        string = []
        for intNum in array:
            string.append(self.__intToChar(intNum))
        # string = ['a','c','f',...]
        string = ''.join(map(str, string))
        # string = acf...
        return string
