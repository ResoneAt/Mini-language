from lark import Lark, Transformer, Tree, Token


class MiniTransformer(Transformer):
    def start(self, statements):
        # Wrap the statements in a program node and return
        program = {"type": "program", "body": statements}
        return program

    def assign_statement(self, args):
        name = args[0]["value"] if isinstance(args[0], dict) else args[0].children[0].value
        value = args[1]["value"] if isinstance(args[1], dict) else args[1].children[0].value
        return {"type": "assignment", "name": name, "value": int(value)}

    def print_statement(self, args):
        # We know print() should always have exactly one argument, which is an expression
        if len(args) == 1:
            value = args[0].children[0].value  # Get the value of the expression inside the print
            return {"type": "print", "value": value}
        else:
            raise ValueError("Print statement should have exactly one argument.")

    def if_statement(self, args):
        # Handling the condition, if-body, and else-body
        condition = args[0]
        if_body = args[1]
        else_body = args[2] if len(args) == 3 else []
        return {
            "type": "if",
            "condition": condition,
            "if_body": if_body,
            "else_body": else_body
        }

    def while_statement(self, args):
        # Handling the condition and body for a while loop
        return {"type": "while", "condition": args[0], "body": args[1]}

    def function_def(self, args):
        # Extract the function name, parameters, and body
        name = args[0].children[0].value
        params = [param.children[0].value for param in args[1:]]  # Extract parameters
        body = args[-1]  # The last argument is the body
        return {"type": "function_def", "name": name, "params": params, "body": body}

    def function_call(self, args):
        # Handle function call by extracting the function name and arguments
        name = None

        # Check if the function name is in the first argument
        if isinstance(args[0], Token):
            name = args[0].value  # If it's a Token, directly get the value
        elif isinstance(args[0], Tree):
            name = args[0].children[0].value  # If it's a Tree, access the first child (function name)

        if name is None:
            raise ValueError("Function name not found")

        # Extract arguments, which could be a Token or Tree
        arguments = []
        for arg in args[1:]:
            if isinstance(arg, Token):
                arguments.append(arg.value)  # If it's a Token, get its value
            elif isinstance(arg, Tree):
                arguments.append(arg.children[0].value)  # If it's a Tree, get the value of the first child

        return {"type": "function_call", "name": name, "arguments": arguments}

    def expression(self, args):
        # Just return the first element of args, which is the expression
        return args[0]

    def STRING(self, token):
        # Strip the surrounding quotes from the string token
        return {"type": "string", "value": str(token)[1:-1]}  # Remove the surrounding quotes

    def IDENTIFIER(self, token):
        return {"type": "identifier", "value": str(token)}

    def NUMBER(self, token):
        return {"type": "number", "value": int(token)}

    # Handle any unprocessed nodes by returning them as dictionaries
    def __default__(self, tree, children, meta):
        if isinstance(tree, Tree):
            return {tree.data: children}  # Wrap children in a dictionary with node data as key
        elif isinstance(tree, Token):
            return {"type": "token", "value": tree.value}  # Return token value as dictionary
        return tree  # Return the tree if no other cases match


class MiniParser:
    def __init__(self, tokens):
        self.tokens = tokens
        grammar_path = "mini/parser/grammar.lark"
        with open(grammar_path, "r") as file:
            grammar = file.read()
        self.parser = Lark(grammar, start="start")

    def parse(self):
        source_code = " ".join(token["value"] for token in self.tokens)
        tree = self.parser.parse(source_code)
        transformer = MiniTransformer()
        ast = transformer.transform(tree)
        return ast

