from lexer import Lexer

if __name__ == '__main__':

    file_name = "input.nullr"
    with open(file_name) as file:
        input_code = file.read()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(input_code)

    for token in tokens:
        print(token)
