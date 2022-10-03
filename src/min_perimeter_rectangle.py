
def divisors(n):
    i = 1
    result = []
    while (i * i < n):
        if (n % i == 0):
            result.append(i)
        i += 1
    if (i * i == n):
        result.append(i)
    return result


def solution(N):
    #https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/
    # Leverage the divisor method from count factors

    n_divs = divisors(N)

    min_perim = N * 4
    for i in n_divs:
        nxt = N / i
        perim = (i + nxt) * 2
        min_perim = min(perim, min_perim)
    return min_perim




    return int((n_divs[0] + n_divs[1]) * 2)