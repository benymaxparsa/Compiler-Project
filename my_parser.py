from rply import ParserGenerator

from ast import Number, Sub, Sum, Print


class Parser:
    def __init__(self):
        self.parser_generator = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON', 'SUM', 'SUB'],
            precedence=[('left', ['SUM', 'SUB'])]
        )

    def parse(self):
        @self.parser_generator.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(production):
            return Print(production[2])

        @self.parser_generator.production('expression : expression SUM expression')
        @self.parser_generator.production('expression : expression SUB expression')
        def expression(production):
            left = production[0]
            operator = production[1]
            right = production[2]

            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.parser_generator.production('expression : NUMBER')
        def number(production):
            return Number(production[0].value)

        @self.parser_generator.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.parser_generator.build()
