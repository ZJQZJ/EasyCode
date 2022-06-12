class ShaCode:
    def __init__(self):
        pass

    def encode(self, string, encoding, shaCodeNum, is_print=True):
        from hashlib import sha1, sha224, sha256, sha512, sha384
        if is_print:
            print('Decoding ShaCode is temporarily not supported')
        if shaCodeNum == 'sha1':
            return sha1(string.encode(encoding)).hexdigest()
        elif shaCodeNum == 'sha224':
            return sha224(string.encode(encoding)).hexdigest()
        elif shaCodeNum == 'sha256':
            return sha256(string.encode(encoding)).hexdigest()
        elif shaCodeNum == 'sha512':
            return sha512(string.encode(encoding)).hexdigest()
        elif shaCodeNum == 'sha384':
            return sha384(string.encode(encoding)).hexdigest()
