def fibonacci(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
    return res

# print (fibonacci(1))
# print (fibonacci(10))


class Fibonacci:
    def __init__(self):
        self.memory = {0: 0, 1: 1}

    def __call__(self, n):
        """
        if n is in memory
            - return it
        if n is not in memory
            - calcuate it recursively
            - put it into memory
            - return it
        """
        if n not in self.memory:
            self.memory[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.memory[n]


fib = Fibonacci()
# print (fib(1))
# print (fib(2))
# print (fib(10))
# print (fib(100))

n = 100000
for i in range(2, n, 2):
    fib(i)
    if (i*10)%n == 0:
            print ('   {}%'.format(i*100/n))
print (len(str(fib(n))))



class Factorial:
    def __init__(self):
        self.memory = {0: 1}

    def __call__(self, n):
        if n not in self.memory:
            self.memory[n] = n*self.__call__(n-1)
        return self.memory[n]

# fact = Factorial()
# for i in range(1, 999):
#     fact(i)
# print (fact(1000))