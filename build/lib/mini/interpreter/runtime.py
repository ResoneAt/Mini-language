from mini.interpreter.builtins import add_builtin_functions
from mini.utils.errors import RuntimeError


class MiniRuntime:
    def __init__(self):
        self.variables = {}  # Holds variables and their values
        self.functions = {}  # Holds user-defined and built-in functions
        add_builtin_functions(self)

    def execute(self, node):
        method_name = f"execute_{node['type']}"
        method = getattr(self, method_name, self.generic_execute)
        return method(node)

    def generic_execute(self, node):
        body = node.get("body", [])
        if isinstance(body, list):
            for child in body:
                self.execute(child)
        else:
            raise RuntimeError("Expected 'body' to be a list of nodes.")

    def execute_assignment(self, node):
        self.variables[node["name"]] = self.evaluate(node["value"])

    def execute_print(self, node):
        value = self.evaluate(node["value"])
        if "print" in self.functions:
            self.functions["print"](value)
        else:
            raise RuntimeError("Print function is undefined.")

    def execute_if(self, node):
        condition = self.evaluate(node["condition"])
        if condition:
            self.execute({"type": "block", "body": node["if_body"]})
        elif "else_body" in node:
            self.execute({"type": "block", "body": node["else_body"]})

    def execute_while(self, node):
        while self.evaluate(node["condition"]):
            self.execute({"type": "block", "body": node["body"]})

    def execute_function_def(self, node):
        self.functions[node["name"]] = {"params": node["params"], "body": node["body"]}

    def execute_function_call(self, node):
        func = self.functions.get(node["name"])
        if not func:
            raise RuntimeError(f"Undefined function '{node['name']}' called at {node}")

        if len(func["params"]) != len(node["args"]):
            raise RuntimeError(
                f"Function '{node['name']}' expects {len(func['params'])} arguments, but {len(node['args'])} were provided.")

        args = {param: self.evaluate(arg) for param, arg in zip(func["params"], node["args"])}
        old_variables = self.variables.copy()
        self.variables.update(args)

        result = None
        for child in func["body"]:
            result = self.execute(child)
            if "return" in child:  # Handle return explicitly
                return result

        self.variables = old_variables
        return result

    def execute_return(self, node):
        return self.evaluate(node["value"])

    def evaluate(self, node):
        node_type = node["type"]
        if node_type == "number":
            return node["value"]
        elif node_type == "string":
            return node["value"]
        elif node_type == "name":
            value = self.variables.get(node["value"])
            if value is None:
                raise RuntimeError(f"Undefined variable '{node['value']}'")
            return value
        elif node_type == "binary_op":
            left = self.evaluate(node["left"])
            right = self.evaluate(node["right"])
            operator = node["operator"]
            return self.evaluate_operator(left, operator, right)
        elif node_type == "return":
            return self.evaluate(node["value"])
        raise RuntimeError(f"Unknown node type: {node_type}")

    def evaluate_operator(self, left, operator, right):
        if operator == "+":
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            elif isinstance(left, list) and isinstance(right, list):
                return left + right
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        if operator == "/":
            return left / right
        raise RuntimeError(f"Unsupported operator: {operator} between {left} and {right}")

    def add_builtin_functions(self):
        # Ensure 'print' is a callable function
        self.functions["print"] = lambda value: print(value)
