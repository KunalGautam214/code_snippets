# What is decorator?
# A decorator is a function that takes another function (or method) as an argument and extends or alters its behavior.
# Decorators allow for the addition of functionality to functions or methods in a clean, readable, and reusable manner.

class SmartDivide:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        if b == 0:
            return 'Oops! can not divide because b is zero'
        return self.func(a, b)


@SmartDivide
def divide(a, b):
    return a / b


print(divide(5, 10))
print(divide(5, 0))
