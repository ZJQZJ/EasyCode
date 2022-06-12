class Base16Code:
    def __init__(self):
        pass

    def base16_encode(self, string, encoding):
        from base64 import b16encode
        return b16encode(string.encode(encoding)).decode(encoding)

    def base16_decode(self, string, encoding):
        from base64 import b16decode
        return b16decode(string.encode(encoding)).decode(encoding)