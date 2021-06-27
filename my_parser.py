from rply import ParserGenerator

from abstract_syntax_tree import Number, Sub, Sum, Div, Mul, Print


class Parser:
    def __init__(self):
        self.parser_generator = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON',
             'DIV', 'MUL', 'SUM', 'SUB', 'OPEN_BRACE', 'CLOSE_BRACE', 'IF'],
            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV'])
                        ]
        )

    def parse(self):
        @self.parser_generator.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(production):
            return Print(production[2])

        @self.parser_generator.production('expression : expression SUM expression')
        @self.parser_generator.production('expression : expression SUB expression')
        @self.parser_generator.production('expression : expression MUL expression')
        @self.parser_generator.production('expression : expression DIV expression')
        def expression(production):
            left = production[0]
            operator = production[1]
            right = production[2]

            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)

        @self.parser_generator.production('expression : NUMBER')
        def number(production):
            return Number(production[0].value)

        @self.parser_generator.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.parser_generator.build()
