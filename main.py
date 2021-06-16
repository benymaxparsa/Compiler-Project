from lexer import Lexer
from my_parser import Parser

if __name__ == '__main__':
    file_name = "input.nullr"
    with open(file_name) as file:
        input_code = file.read()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(input_code)

    parser_generator = Parser()
    parser_generator.parse()
    parser = parser_generator.get_parser()
    parser.parse(tokens).eval()
