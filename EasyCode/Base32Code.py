class Base32Code:
    def __init__(self):
        pass

    def base32_encode(self, string, encoding):
        from base64 import b32encode
        return b32encode(string.encode(encoding)).decode(encoding)

    def base32_decode(self, string, encoding):
        from base64 import b32decode
        return b32decode(string.encode(encoding)).decode(encoding)