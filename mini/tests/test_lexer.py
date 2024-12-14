from mini.lexer.lexer import MiniLexer


def test_lexer():
    lexer = MiniLexer("parser/grammar.lark")
    code = 'x = 5\nprint(x)'
    tokens = lexer.tokenize(code)
    assert tokens is not None
