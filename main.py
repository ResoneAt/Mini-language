import sys

from mini.interpreter.runtime import MiniRuntime
from mini.lexer.lexer import Lexer
from mini.parser.parser import MiniParser


class MiniInterpreter:
    def __init__(self):
        self.lexer = None
        self.parser = MiniParser()
        self.runtime = MiniRuntime()

    def run(self, source_code):
        try:
            # Step 1: Lexing
            self.lexer = Lexer(source_code)
            tokens = self.lexer.tokenize()

            # Step 2: Parsing
            ast = self.parser.parse(source_code)

            # Step 3: Execution
            self.runtime.execute(ast)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            source_code = file.read()
        interpreter = MiniInterpreter()
        interpreter.run(source_code)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
