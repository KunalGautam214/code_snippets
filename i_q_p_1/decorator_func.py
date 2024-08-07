# What is decorator?
# A decorator is a function that takes another function (or method) as an argument and extends or alters its behavior.
# Decorators allow for the addition of functionality to functions or methods in a clean, readable, and reusable manner.

def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            return 'Oops! can not divide because b is zero'
        return func(a, b)

    return wrapper


@smart_divide
def divide(a, b):
    return a / b


print(divide(5, 10))
print(divide(5, 0))
