class Morse:
    def __init__(self):
        from EasyCode.MorseCode import MorseCode
        self.code = MorseCode()

    def encode(self, string):
        return self.code.encode(string)

    def decode(self, string):
        return self.code.decode(string)


class Ascll:
    def __init__(self):
        from EasyCode.AscllCode import AscllCode
        self.code = AscllCode()

    def encode(self, string):
        return self.code.encode(string)

    def decode(self, string):
        return self.code.decode(string)


class Base64:
    def __init__(self):
        from EasyCode.Base64Code import Base64Code
        self.code = Base64Code()

    def encode(self, string, encoding):
        return self.code.base64_encode(string, encoding)

    def decode(self, string, encoding):
        return self.code.base64_decode(string, encoding)


class Base32:
    def __init__(self):
        from EasyCode.Base32Code import Base32Code
        self.code = Base32Code()

    def encode(self, string, encoding):
        return self.code.base32_encode(string, encoding)

    def decode(self, string, encoding):
        return self.code.base32_decode(string, encoding)


class Base16:
    def __init__(self):
        from EasyCode.Base16Code import Base16Code
        self.code = Base16Code()

    def encode(self, string, encoding):
        return self.code.base16_encode(string, encoding)

    def decode(self, string, encoding):
        return self.code.base16_decode(string, encoding)


class MD5:
    def __init__(self):
        from EasyCode.MD5 import MD5
        self.code = MD5()

    def encode(self, string, encoding, is_print=True):
        self.code.MD5_encode(string, encoding, is_print)


class ShaCode:
    def __init__(self):
        from ShaCode import ShaCode
        self.code = ShaCode()

    def encode(self, string, encoding, shaCodeNum, is_print=True):
        return self.code.encode(string, encoding, shaCodeNum, is_print)
    