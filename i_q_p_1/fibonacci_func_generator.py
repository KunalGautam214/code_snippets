# What is Generator?
# A generator is a special type of iterator that allows you to iterate over a sequence of values without creating
# and storing the entire sequence in memory at once. Generators provide a convenient way to implement lazy evaluation,
# where values are produced on-the-fly and only when needed, which can save memory and improve performance for large
# datasets.


def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a + b


x = fibonacci(10)
for i in x:
    print(i)

for i in x:
    print(i)
