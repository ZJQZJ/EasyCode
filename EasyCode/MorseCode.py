class MorseCode:
    def __init__(self):
        from EasyCode.PCT import PCT, PCT_KEYS, PCT_VALUES
        self.pct = PCT
        self.pct_keys = PCT_KEYS
        self.pct_values = PCT_VALUES

    def encode(self, string):
        string = string.upper()
        string_list = string.split(' ')
        return_list = []
        for input_str in string_list:
            for str in input_str:
                if str in self.pct_values:
                    return_list.append(self.pct_keys[self.pct_values.index(str)])
                return_list.append('    ')
            return_list.append('        ')
            return_list = ''.join(return_list)
            return_list = list(return_list)
            len_rl = len(return_list)
            num = len_rl - 4
            for i in range(4):
                return_list.pop(num)

        return_list = ''.join(return_list)
        return_list = list(return_list)
        len_rl = len(return_list)
        num = len_rl - 8
        for i in range(8):
            return_list.pop(num)

        return ''.join(return_list)

    def decode(self, string):
        string_list = string.split(' ')
        print(string_list)
        decode_list = []
        space = 0
        for output_str in string_list:
            if output_str in self.pct_keys:
                decode_list.append(self.pct_values[self.pct_keys.index(output_str)])
                space = 0
            else:
                space += 1
            if space == 7:
                space = 0
                decode_list += ' '

        print(space)

        return ''.join(decode_list)
