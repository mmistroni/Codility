#https://app.codility.com/programmers/lessons/13-fibonacci_numbers/ladder/

def fibonacci_seq(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return [f for f in fib if f > 0]


def solution(A, B):
    res  = []
    for step, pwr  in zip(A, B):
        # We need to change this. we are not looking for sum but to see
        # if we are at rung 4
        current_seq = fibonacci_seq(step + 10)

        try:
            num = current_seq[step]
            res.append(num % 2 ** pwr)
        except Exception as e:
            print(f'Exception for {step}: {str(e)}')
    return res
