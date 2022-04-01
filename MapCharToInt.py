import array


class MapCharToInt:
    def __init__(self, string):
        self.string = string

    def char_to_int(char):
        if ord('A') < ord(char) < ord('Z'):
            return int(ord(char) - 65)

        if ord('a') < ord(char) < ord('z'):
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

    def get(self):
        a = array.array
        for char in self.string:
            a.append(self.char_to_int(char))
