class BuiltinFunctions:
    @staticmethod
    def print_fn(*args):
        print(*args)

    @staticmethod
    def len_fn(arg):
        if hasattr(arg, '__len__'):
            return len(arg)
        raise TypeError("Argument to 'len' must be iterable.")

    @staticmethod
    def sum_fn(arg):
        if isinstance(arg, (list, tuple)):
            return sum(arg)
        raise TypeError("Argument to 'sum' must be a list or tuple.")

    @staticmethod
    def range_fn(start, end):
        return list(range(start, end))


def add_builtin_functions(runtime):
    runtime.functions["print"] = BuiltinFunctions.print_fn
    runtime.functions["len"] = BuiltinFunctions.len_fn
    runtime.functions["sum"] = BuiltinFunctions.sum_fn
    runtime.functions["range"] = BuiltinFunctions.range_fn
