class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOperator:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class Sum(BinaryOperator):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOperator):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
