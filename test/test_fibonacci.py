import unittest


def fibonacci(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def fibonacci2(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(1, 100):
            print(f'{fibonacci(i)} vs {fibonacci2(i)}')



if __name__ == '__main__':
    unittest.main()
