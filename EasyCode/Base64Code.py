class Base64Code:
    def __init__(self):
        pass

    def base64_encode(self, string, encoding):
        from base64 import b64encode
        return b64encode(string.encode(encoding)).decode(encoding)

    def base64_decode(self, string, encoding):
        from base64 import b64decode
        return b64decode(string.encode(encoding)).decode(encoding)