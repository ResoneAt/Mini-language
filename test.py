from mini.lexer.lexer import Lexer
from mini.parser.parser import MiniParser

# Input tokens for assignment: x = 2
tokens = [
    {"value": "x"},
    {"value": "="},
    {"value": "2"}
]

parser = MiniParser(tokens)  # Initialize the parser with tokens
ast = parser.parse()  # Get the AST
print("Transformed AST:", ast)  # Visualize the AST to ensure it's correct
