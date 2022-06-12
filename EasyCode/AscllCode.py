class AscllCode:
    def __init__(self):
        pass

    def encode(self, string):
        ret = []
        for i in string:
            ret.append(str(ord(i)))
            ret.append(' ')
        return ''.join(ret)

    def decode(self, string):
        ret = []
        new = []
        a = ''
        for i in string:
            if i != ' ':
                a += i
            else:
                new.append(a)
                a = ''
        for i in new:
            if i != ' ':
                ret.append(chr(int(i)))
        return ''.join(ret)
