class MiniError(Exception):
    """Base class for all Mini language errors."""
    pass


class SyntaxError(MiniError):
    """Raised when there is a syntax error in the source code."""
    def __init__(self, message):
        super().__init__(f"Syntax Error: {message}")


class RuntimeError(MiniError):
    """Raised during runtime execution."""
    def __init__(self, message):
        super().__init__(f"Runtime Error: {message}")


class TypeError(MiniError):
    """Raised for type mismatch errors."""
    def __init__(self, message):
        super().__init__(f"Type Error: {message}")
