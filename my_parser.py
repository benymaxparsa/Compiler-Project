from rply import ParserGenerator

from abstract_syntax_tree import Number, Sub, Sum, Div, Mul, Print


class Parser:
    def __init__(self, module, builder, printf):
        self.parser_generator = ParserGenerator(
            ['PI', 'FLOAT', 'INTEGER', 'STRING', 'BOOLEAN',
             'SUM', 'SUB', 'MUL', 'DIV', 'AND', 'OR',
             '==', '!=', '<=', '>=', '>', '<', '=',
             'IF', 'ELSE', ';', ',', '(', ')', '{', '}',
             'INPUT', 'FUNCTION', 'PRINT', 'ABSOLUTE',
             'POWER', 'SIN', 'COS', 'VAR', 'IDENTIFIER'],
            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV']),
                ('left', ['FUNCTION']),
                ('left', ['VAR']),
                ('left', ['=']),
                ('left', ['IF', 'ELSE', ';']),
                ('left', ['AND', 'OR']),
                ('left', ['==', '!=', '>=', '>', '<', '<=']),
                ('left', ['STRING', 'INTEGER', 'FLOAT', 'BOOLEAN', 'PI'])
                        ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.parser_generator.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(production):
            return Print(self.builder, self.module, self.printf, production[2])

        @self.parser_generator.production('expression : expression SUM expression')
        @self.parser_generator.production('expression : expression SUB expression')
        @self.parser_generator.production('expression : expression MUL expression')
        @self.parser_generator.production('expression : expression DIV expression')
        def expression(production):
            left = production[0]
            operator = production[1]
            right = production[2]

            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)

        @self.parser_generator.production('expression : NUMBER')
        def number(production):
            return Number(self.builder, self.module, production[0].value)

        @self.parser_generator.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.parser_generator.build()
