from scanner import Lexer
from my_parser import Parser
from codegen import CodeGen

if __name__ == '__main__':
    file_name = "input.nullr"
    with open(file_name) as file:
        input_code = file.read()

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(input_code)

    codegen = CodeGen()
    module = codegen.module
    builder = codegen.builder
    printf = codegen.print

    parser_generator = Parser(module, builder, printf)
    parser_generator.parse()
    parser = parser_generator.get_parser()
    parser.parse(tokens).eval()

    codegen.create_ir()
    codegen.save_ir("IrFile.ll")
