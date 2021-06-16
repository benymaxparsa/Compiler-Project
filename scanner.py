from rply import LexerGenerator


class Lexer:

    def __init__(self):
        self.lexer = LexerGenerator()

    def add_tokens(self):
        self.lexer.add('PRINT', r'Print')
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.ignore('\s+')
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('SEMI_COLON', r'\;')

    def get_lexer(self):
        self.add_tokens()
        return self.lexer.build()
