import unittest


def fibonacci(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

def fibonacci2(n):
    if n == 0:
        return 0
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(0, 10):
            print(f'1-{fibonacci2(i)} vs 2-{fibonacci(i)}')


if __name__ == '__main__':
    unittest.main()
