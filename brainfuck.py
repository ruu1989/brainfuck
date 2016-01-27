ALLOWED_CHARS = ['.', ',', '[', ']', '<', '>', '+', '-']


class UnexpectedCharacterException(Exception):
    def __init__(self, index, char):
        self.index = index
        self.char = char

    def __str__(self):
        return 'Error: Character {char} found at pos {index} is not valid in Brainfuck'.format(
            char=self.char,
            index=self.index
        )


def parse(code):

    chars = [char for char in code]

    for index, char in enumerate(chars):
        if char not in ALLOWED_CHARS:
            raise UnexpectedCharacterException(index, char)

    # Need to store a pointer to indicate where we are in the code. Can't just iterate through
    # the chars as we need to be able to move about to handle the []'s.
    code_pointer = 0

    cells = [0]
    pointer = 0

    while code_pointer < len(chars):
        command = chars[code_pointer]

        if command == '>':
            pointer += 1
            if len(cells) <= pointer:
                cells.append(0)

        if command == '<':
            pointer = pointer - 1 if pointer > 0 else 0

        if command == '+':
            cells[pointer] = cells[pointer] + 1 if cells[pointer] < 255 else 0

        if command == '-':
            cells[pointer] = cells[pointer] - 1 if cells[pointer] > 0 else 255

        if command == '.':
            print(chr(cells[pointer]))

        if command == ',':
            new_char = ''
            while len(new_char) != 1:
                new_char = raw_input('Enter a char: ')

            cells[pointer] = new_char

        code_pointer += 1


if __name__ == '__main__':
    try:
        parse('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++..')
    except UnexpectedCharacterException as e:
        print(e)
