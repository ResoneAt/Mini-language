from mini.interpreter.runtime import MiniRuntime
from mini.lexer.lexer import Lexer
from mini.parser.parser import MiniParser


def start_repl():
    print("Welcome to the Mini Interpreter! Type 'exit' to quit.")
    runtime = MiniRuntime()

    while True:
        try:
            # Read user input
            source_code = input(">>> ")
            if source_code.lower() in ("exit", "quit"):
                print("Exiting the Mini Interpreter. Goodbye!")
                break

            # Tokenize and parse the input
            lexer = Lexer(source_code)
            tokens = lexer.tokenize()

            parser = MiniParser(tokens)
            ast = parser.parse()
            runtime.execute(ast)

        except Exception as e:
            print(f"Error: {e}")
