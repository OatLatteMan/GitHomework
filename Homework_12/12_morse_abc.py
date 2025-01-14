alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}

alphabet_reverse = {value: key for key, value in alphabet.items()}


class Morse:
    def encode(self, text: str):
        self.text = text.upper()
        self.the_list = []
        self.new_str = ''

        for i in self.text:
            self.the_list += i

        for i in self.the_list:
            self.new_str += alphabet[i]

        return self.new_str

    def decode(self, morse):
        pass

morse = Morse()
print(morse.encode('SOME TEXT HERE'))

# print(morse.decode('... --- -- .   - . -..- -   .... . .-. .'))
# print(morse.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))