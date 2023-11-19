characters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z',
                   '[', ']', '{', '}', '(', ')', "'", '"', '_', ',', '+', '-', '*', '/', '.', ' ',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class CatCompile:
    def __init__(self, string_, key):
        self.string = string_
        self.key = key
        self.code = []
        self.letters_symbols_numbers()

    def letters_symbols_numbers(self):
        cats = ""
        num = 0
        for char in self.string:
            if char != ";":
                cats += char
                if self.key in cats:
                    num += 1
                    cats = ""
            else:
                if num > 0:
                    temp = characters_list[num - 1]
                    self.code.append(temp)
                    num = 0
        if num > 0:
            temp = characters_list[num - 1]
            self.code.append(temp)
        result_string = ''.join(self.code)
        return result_string

    def get_result(self):
        return ''.join(self.code)


key = input("key = ")
while True:
    input_string = input("cat++ > ")
    if input_string != "cat cat cat cat cat; cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat; cat cat cat cat cat cat cat cat cat; cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat cat":
        break
    command = CatCompile(input_string, key)
    result = command.get_result()
    exec(result)
print("cat ate food.")
