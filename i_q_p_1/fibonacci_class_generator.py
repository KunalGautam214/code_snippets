# What is Generator?
# A generator is a special type of iterator that allows you to iterate over a sequence of values without creating
# and storing the entire sequence in memory at once. Generators provide a convenient way to implement lazy evaluation,
# where values are produced on-the-fly and only when needed, which can save memory and improve performance for large
# datasets.

class Fibonacci:
    def __init__(self, limit):
        self.a = 0
        self.b = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration

    def fib(self):
        while self.a < self.limit:
            yield self.a
            self.a, self.b = self.b, self.a + self.b


f = Fibonacci(10)
for i in f.fib():
    print(i)
