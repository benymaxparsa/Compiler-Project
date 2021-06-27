from llvmlite import ir


class Number:
    def __init__(self, builder, module, value):
        self.value = value
        self.builder = builder
        self.module = module

    def eval(self):
        return ir.Constant(ir.IntType(8), int(self.value))


class BinaryOperator:
    def __init__(self, builder, module, left, right):
        self.right = right
        self.left = left
        self.builder = builder
        self.module = module


class Sum(BinaryOperator):
    def eval(self):
        return self.builder.add(self.left.eval(), self.right.eval())


class Sub(BinaryOperator):
    def eval(self):
        return self.builder.sub(self.left.eval(), self.right.eval())


class Mul(BinaryOperator):
    def eval(self):
        return self.builder.mul(self.left.eval(), self.right.eval())


class Div(BinaryOperator):
    def eval(self):
        return self.builder.sdiv(self.left.eval(), self.right.eval())


class Print:
    def __init__(self, builder, module, printf, value):
        self.value = value
        self.builder = builder
        self.module = module
        self.printf = printf

    def eval(self):
        value = self.value.eval()

        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        self.builder.call(self.printf, [fmt_arg, value])
