import re
class Token:
    def __init__(self, t, v):
        self.type = t
        self.value = v

    def __str__(self):
        return 'Token = `{}\' : `{}\''.format(self.type, self.value)

class Lexer:
    _keyword = ['let', 'def', 'if', 'elsif', 'else', 'end']
    _literal = ['nil', 'true', 'false']
    def __init__(self, program):
        self._program = program
        self._index = 0
        self._len = len(program)

    def get_token(self):
        while True:
            if self._index >= self._len:
                raise StopIteration

            curr_char = self._program[self._index]
            # skip space
            if curr_char.isspace():
                self._index += 1
                continue
            
            r_identifier = r'[_a-zA-Z][_a-zA-Z0-9]*'
            match = re.match(r_identifier, self._program[self._index:])
            if match is not None:
                self._index += match.end()
                identifier = match.group() 
                if identifier in self._keyword:
                    return Token(identifier, identifier)
                return Token('Identifier', identifier)

            r_number = r'[-+]?[0-9]*\.?[0-9]+'
            match = re.match(r_number, self._program[self._index:])
            if match is not None:
                self._index += match.end()
                number = match.group() 
                return Token('Number', float(number))

            r_arrow = r'=>'
            match = re.match(r_arrow, self._program[self._index:])
            if match is not None:
                self._index += match.end()
                number = match.group() 
                return Token('Arrow', '=>')

            r_arrow = r':='
            match = re.match(r_arrow, self._program[self._index:])
            if match is not None:
                self._index += match.end()
                number = match.group() 
                return Token('Assign', ':=')

            self._index += 1
            return Token(curr_char, curr_char)

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_token()


program = '''
let a = 5
a := 6
def do_0(x)
  x * 2
end
if true
  do_1()
elsif false
  do_2()
else
  do_3()
end
'''
lexer = Lexer(program)
for token in lexer:
    print(token)
