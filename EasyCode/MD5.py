class MD5:
    def __init__(self):
        pass

    def MD5_encode(self, string, encoding, is_print=True):
        from hashlib import md5
        if is_print:
            print('Decoding MD5 is temporarily not supported')
        return md5(string.encode(encoding)).hexdigest()
