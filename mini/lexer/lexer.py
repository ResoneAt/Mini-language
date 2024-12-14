import re


class Lexer:
    TOKENS = [
        (r'[ \t\n]+', None),                 # Whitespace
        (r'#.*', None),                      # Comments
        (r'[0-9]+', 'NUMBER'),               # Numbers
        (r'"[^"]*"', 'STRING'),              # Strings
        (r'[\w_]+', 'IDENTIFIER'),           # Identifiers
        (r'[\+\-\*/=<>!]+', 'OPERATOR'),     # Operators
        (r'[(){}.,]', 'PUNCTUATION'),        # Punctuation
    ]

    def __init__(self, source_code):
        self.source_code = source_code
        self.line = 1
        self.column = 1

    def tokenize(self):
        tokens = []
        index = 0
        while index < len(self.source_code):
            match = None
            for regex, token_type in self.TOKENS:
                match = re.match(regex, self.source_code[index:])
                if match:
                    value = match.group(0)
                    if token_type:
                        tokens.append({
                            "type": token_type,
                            "value": value,
                            "line": self.line,
                            "column": self.column
                        })
                    index += len(value)
                    self.update_position(value)
                    break
            if not match:
                raise SyntaxError(
                    f"Unexpected character '{self.source_code[index]}' "
                    f"at line {self.line}, column {self.column}"
                )
        return tokens

    def update_position(self, text):
        lines = text.splitlines()
        if len(lines) > 1:
            self.line += len(lines) - 1
            self.column = len(lines[-1]) + 1
        else:
            self.column += len(lines[-1])
