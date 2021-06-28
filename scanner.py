from rply import LexerGenerator


class Lexer:

    def __init__(self):
        self.lexer = LexerGenerator()

    def add_tokens(self):
        # const and data types
        self.lexer.add('PI', r'-?__PI__')
        self.lexer.add('FLOAT', r'-?\d+\.\d+')
        self.lexer.add('INTEGER', r'-?\d+')
        self.lexer.add('STRING', r'(".*")')
        self.lexer.add('BOOLEAN', r'true(?!\w)|false(?!\w)')
        # math Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        # binary operators
        self.lexer.add('AND', r'and(?!\w)')
        self.lexer.add('OR', r'or(?!\w)')
        self.lexer.add('==', r'\=\=')
        self.lexer.add('!=', r'\!\=')
        self.lexer.add('<=', r'\<\=')
        self.lexer.add('>=', r'\>\=')
        self.lexer.add('>', r'\>')
        self.lexer.add('<', r'\<')
        self.lexer.add('=', r'\=')
        # statement
        self.lexer.add('IF', r'if(?!\w)')
        self.lexer.add('ELSE', r'else(?!\w)')
        self.lexer.add('FOR', r'for(?!\w)')
        # punctuation
        self.lexer.add(';', r'\;')
        self.lexer.add(',', r'\,')
        self.lexer.add('(', r'\(')
        self.lexer.add(')', r'\)')
        self.lexer.add('{', r'\{')
        self.lexer.add('}', r'\}')
        # functions
        self.lexer.add('INPUT', r'Input')
        self.lexer.add('FUNCTION', r'Function')
        self.lexer.add('PRINT', r'Print')
        self.lexer.add('ABSOLUTE', r'Abs')
        self.lexer.add('POWER', r'Pow')
        self.lexer.add('SIN', r'Sin')
        self.lexer.add('COS', r'Cos')
        self.lexer.add('DOT', r'Dot')
        self.lexer.add('CROSS', r'Cross')
        # assigner
        self.lexer.add('VAR', r'var(?!\w)')
        self.lexer.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]*")
        # ignore white spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self.add_tokens()
        return self.lexer.build()
