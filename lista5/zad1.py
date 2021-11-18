from math import log


class LogExp:
    def __init__(self, a):
        self.a = a

    def logarithm(self, x=1):
        return log(x, self.a)

    def expotentiation(self, x=1):
        return self.a ** x


num1 = LogExp(10)
print(num1.logarithm(100), num1.expotentiation(3), num1.expotentiation())
